#!/usr/bin/env python

import os
import sys
import json
import yaml
import random

class Block:
   def __init__(self, data):
      self.next = None
      if 'children' in data:
         self.child = data['children'][0]

         i = 1
         while i < len(data['children']):
            data['children'][i-1].next = data['children'][i]
            i += 1

   def run(self, state):
      print "ERROR: Block run() called"
      return self.next

random_stack = []
choice_stack = []

def run_sequence(seq, state):
   global random_stack
   global choice_stack
   b = seq
   while b:
      b = b.run(state)
      if len(random_stack) > 0 and not isinstance(b, Random) and not isinstance(b, Conditional):
         b = random.choice(random_stack)
         random_stack = []
      elif len(choice_stack) > 0 and not isinstance(b, Choice) and not isinstance(b, Conditional):
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

class Sequence(Block):
   def __init__(self, data):
      self.child = None
      Block.__init__(self, data)
      self.name = data['content']

   def run(self, state):
      if self.child:
         run_sequence(self.child, state)
      return self.next

class Link(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.target = data['content']

class Comment(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.comment = data['content']

   def run(self, state):
      # explicitly do nothing
      return self.next

class Flag(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      print "TODO: Flag constructor called"

class Conditional(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      print "TODO: better conditional parser"
      t = data['type']
      if t == 'condition' or t == 'condition_call':
         pass

class Choice(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.text = data['content']

   def run(self, state):
      i = len(choice_stack) + 1
      print "%d) %s"%(i, self.text)
      choice_stack.append(self.child)
      return self.next

class Random(Block):
   def run(self, state):
      random_stack.append(self.child)
      return self.next

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

class Increment(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.variable = data['variable']

   def run(self, state):
      state[self.variable] += 1
      return self.next

class Assignment(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.variable = data['variable']
      self.value = data['value']

   def run(self, state):
      state[self.variable] = self.value
      return self.next

# Text classes
class Text(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.text = data['content']

   def run(self, state):
      print self.text
      print
      return self.next

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

def get_sections(data, sections):
   while data:
      data = data.next
   

def main():
   if len(sys.argv) != 2:
      print "Usage: aucuba <json>"
      sys.exit(1)

   # load the data
   data = json.load(open(sys.argv[1]), object_hook=parse_hook)

   # set up the next pointers
   main_data = data['sequences']['main']
   sections = {}

   print yaml.dump(main_data)

   print
   print "Done loading data. Running"
   print

   state = {}
   run_sequence(main_data, state)

if __name__ == '__main__':
   main()
