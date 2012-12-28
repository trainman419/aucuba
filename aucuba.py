#!/usr/bin/env python

import os
import sys
import json
import yaml
import random

block_id = 0

class Block:
   def __init__(self, data):
      self.next = None
      global block_id
      self.id = block_id
      block_id += 1
      if 'children' in data:
         self.child = data['children'][0]

         i = 1
         while i < len(data['children']):
            data['children'][i-1].next = data['children'][i]
            i += 1

   def run(self, state):
      print "ERROR: Block run() called on ", self
      return self.next

   def java(self):
      print "ERROR: Block print() called on ", self
      return "\n"

stack = []
random_stack = []
choice_stack = []

def run_sequence(seq, state):
   global random_stack
   global choice_stack
   b = seq
   while b:
      b = b.run(state)
      if not b and len(stack) > 0:
         b = stack.pop()
      if len(random_stack) > 0 and not isinstance(b, Random) and not isinstance(b, Conditional):
         if b:
            stack.append(b)
         b = random.choice(random_stack)
         random_stack = []
      elif len(choice_stack) > 0 and not isinstance(b, Choice) and not isinstance(b, Conditional):
         if b:
            stack.append(b)

         print
         # Get input from the user. Prompt them until the give us an answer we
         # like
         i = None
         while i is None:
            try:
               i = int(raw_input('> '))
            except ValueError:
               i = 0
            if i < 1 or i > len(choice_stack):
               print "Please enter a number between 1 and %d"%(len(choice_stack))
               i = None

         b = choice_stack[i-1] 
         choice_stack = []
      if not b and len(stack) > 0:
         b = stack.pop()

def java(block_id, block_type, *args):
   return "Block block_%s = new %s(%s);\n"%(block_id, block_type, 
         ", ".join(args))

def block_name(block):
   if block:
      return "block_%d"%(block.id)
   else:
      return "null"


class Sequence(Block):
   def __init__(self, data):
      self.child = None
      Block.__init__(self, data)
      self.name = data['content']

   def run(self, state):
      if self.child:
         stack.append(self.next)
         return self.child
      return self.next

   def java(self):
      return java(self.id, "Sequence", block_name(self.next),
            block_name(self.child), '"%s"'%self.name)


class Link(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.target = data['content']

   def run(self, state):
      global stack
      stack = []
      return self.next

   def java(self):
      return java(self.id, "Link")

class Comment(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.comment = data['content']

   def run(self, state):
      # explicitly do nothing
      return self.next

   def java(self):
      return "";

class Flag(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.variable = data['variable']

   def java(self):
      return java(self.id, 'Flag', block_name(self.next), 
            '"%s"'%(self.variable))

functions = {
      'no': lambda x: x == 0,
      'with_ally': lambda : False,
      '': lambda: True,
      'not': lambda x: not x,
      'use_magic': lambda x: bool(x)}

class Conditional(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      t = data['type']
      if t == 'condition':
         print "ERROR: can't deal with condition"
         pass
      elif t == 'condition_call':
         self.function = data['call']
         self.arguments = data['arguments']
      else:
         print "ERROR: can't deal with fallback/default conditionals"
   
   def run(self, state):
      global stack
      if hasattr(self, 'function'):
         args = map(lambda x: state[x], self.arguments)
         if self.function in functions:
            if functions[self.function](*args):
               if self.next:
                  stack.append(self.next)
               return self.child
            else:
               return self.next
         elif len(args) == 0 and self.function in state:
            # FIXME: hack to deal with conditionals not being parsed properly
            if state[self.function]:
               if self.next:
                  stack.append(self.next)
               return self.child
            else:
               return self.next
         else:
            print "ERROR: Undefined function %s"%(self.function)
      else:
         print "TODO: conditional run. Condition unknown"
      return self.next

   def java(self):
      s = 'null'
      output = ""
      if len(self.arguments) > 0:
         s = "args_%d"%(self.id)
         output += "String [] %s = new String[%d];\n"%(s, len(self.arguments))
         for i,a in enumerate(self.arguments):
            output += "%s[%d] = \"%s\";\n"%(s, i, a)
      output += java(self.id, "Conditional", block_name(self.next),
            block_name(self.child), '"%s"'%self.function, s)
      return output;

class Choice(Block):
   def __init__(self, data):
      self.child = None
      Block.__init__(self, data)
      self.text = data['content']

   def run(self, state):
      i = len(choice_stack) + 1
      print "%d) %s"%(i, self.text)
      choice_stack.append(self.child)
      return self.next

   def java(self):
      print "TODO: convert choice text to id"
      return java(self.id, "Choice", block_name(self.next), 
            block_name(self.child), '0')

class Random(Block):
   def run(self, state):
      random_stack.append(self.child)
      return self.next

   def java(self):
      return java(self.id, "Random", block_name(self.next),
            block_name(self.child))

# Expressions
class Call(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      print "TODO: implement call constructor"

class Decrement(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.variable = data['variable']

   def run(self, state):
      state[self.variable] -= 1
      return self.next

   def java(self):
      return java(self.id, 'Decrement', block_name(self.next), 
            '"%s"'%(self.variable))

class Increment(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.variable = data['variable']

   def run(self, state):
      state[self.variable] += 1
      return self.next

   def java(self):
      return java(self.id, 'Increment', block_name(self.next), 
            '"%s"'%(self.variable))

class Assignment(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.variable = data['variable']
      self.value = data['value']

   def run(self, state):
      try:
         state[self.variable] = int(self.value)
      except:
         state[self.variable] = self.value
      return self.next

   def java(self):
      v = '"%s"'%(self.value)
      try:
         v = "%d"%(int(self.value))
      except:
         try:
            if bool(self.value):
               v = 'true'
            else:
               v = 'false'
         except:
            pass
      output = "AsherahValue value_%s = new AsherahValue(%s);\n"%(self.id, v)
      output += java(self.id, 'Assignment', block_name(self.next), 
            '"%s"'%(self.variable), 'value_%s'%(self.id))
      return output

# Text classes
class Text(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.text = data['content']

   def run(self, state):
      print self.text
      print
      return self.next

   def java(self):
      print "TODO: convert text to id"
      return java(self.id, 'Text', block_name(self.next), '0')

class Descriptive(Text):
   pass

class Action(Text):
   pass

class Narration(Text):
   pass

class Speech(Text):
   def __init__(self, data):
      Text.__init__(self, data)
      self.actor = data['actor']
      self.text = "%s: %s"%(self.actor, self.text)


type_map = {
      'sequence':             Sequence,
      'link':                 Link,
      'decrement':            Decrement,
      'increment':            Increment,
      'assignment':           Assignment,
      'comment':              Comment,
      'action':               Action,
      'choice':               Choice,
      'condition':            Conditional,
      'condition_call':       Conditional,
      'condition_default':    Conditional,
      'condition_fallback':   Conditional,
      'call':                 Call,
      'random':               Random,
      'random_block':         Random,
      'descriptive':          Descriptive,
      'narration':            Narration,
      'speech':               Speech,
      'flag':                 Flag
      }

def parse_hook(data):
   # Parse block objects
   if 'type' in data:
      t = data['type']
      if t in type_map:
         d = type_map[t](data)
         return d
      else:
         print "Got unknown type: %s"%(t)
   # Explicit case for top-level object
   elif 'sequences' in data:
      # TODO: real object for top-level object
      return data
   elif 'main' in data:
      # TODO: real object for top-level sequences
      out = {}
      for seq in data:
         d = { 'type': 'sequence', 'content': seq, 'children': data[seq]}
         out[seq] = Sequence(d)
      return out
   else:
      print "Got malformed data: ", data
   print
   return data

def map_tree(data, func):
   while data:
      func(data)
      if hasattr(data, 'child'):
         map_tree(data.child, func)
      if isinstance(data, Link):
         data = None
      else:
         data = data.next

def get_sections(data, sections):
   if isinstance(data, Sequence):
      if not data.name in sections:
         sections[data.name] = data

def set_links(data, sections):
   if isinstance(data, Link):
      data.next = sections[data.target]

def write_java_defs(data):
   output = ""
   if hasattr(data, 'child') and data.child:
      output += write_java_defs(data.child)
   if data.next and not isinstance(data, Link):
      output += write_java_defs(data.next)
   output += data.java()
   return output

def main():
   if len(sys.argv) != 2:
      print "Usage: aucuba <json>"
      sys.exit(1)

   # load the data
   data = json.load(open(sys.argv[1]), object_hook=parse_hook)

   # set up the next pointers
   sequences = data['sequences']
   sections = {}

   for seq in sequences:
      map_tree(sequences[seq], lambda d: get_sections(d, sections))

   for seq in sequences:
      map_tree(sequences[seq], lambda d: set_links(d, sections))


   # HACK FIXME TODO: set the next link in each sequence. This is ARBITRARY
   #  based on the order of the keys in the sequences dict
   d = None
   for seq in sequences:
      if d:
         d.next = sequences[seq]
      d = sequences[seq]

   print
   print "Done loading data. Running"
   print

   for seq in sequences:
      print write_java_defs(sequences[seq])

#   state = {}
#   for var in data['variables']:
#      state[var] = False
#
#   try:
#      run_sequence(sections['main'], state)
#   except KeyboardInterrupt:
#      print
#      print "Done"
#   except EOFError:
#      print "Done"

if __name__ == '__main__':
   main()
