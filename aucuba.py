#!/usr/bin/env python

import os
import sys
import json
import yaml

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
      print dir(self)
      return self.next

class Sequence(Block):
   def __init__(self, data):
      self.children = []
      Block.__init__(self, data)
      self.name = data['content']

   def run(self, state):
      if len(self.children) > 0:
         b = self.children[0]
         while b:
            b = b.run()

class Link(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.target = data['content']

class Comment(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.comment = data['content']

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

class Random(Block):
   pass

# Expressions
class Call(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      print "TODO: implement call constructor"

class Decrement(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.variable = data['variable']

class Increment(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.variable = data['variable']

class Assignment(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.variable = data['variable']
      self.value = data['value']

# Text classes
class Text(Block):
   def __init__(self, data):
      Block.__init__(self, data)
      self.text = data['content']

   def run(self, state):
      print self.text

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

   def run(self, state):
      print "%s: %s"%(self.actor, self.text)


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
      print "Got toplevel object: ", data
      return data
   elif 'main' in data:
      print "Got sequences: ", data
      return data
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
   b = main_data[0]
   while b:
      b = b.run(state)

if __name__ == '__main__':
   main()
