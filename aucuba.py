#!/usr/bin/env python

import os
import sys
import json

class Block:
   def __init__(self, data):
      if 'children' in data:
         self.children = data['children']
         print "Got children: ", self.children
      print "ERROR: Block __init__ called"

   def run(self):
      print "ERROR: Block run() called"

class Sequence(Block):
   def __init__(self, data):
      self.name = data['content']

class Link(Block):
   def __init__(self, data):
      self.target = data['content']

class Comment(Block):
   def __init__(self, data):
      self.comment = data['content']

class Flag(Block):
   def __init__(self, data):
      print "ERROR: Flag constructor called"

class Conditional(Block):
   def __init__(self, data):
      print "TODO: better conditional parser"

class Choice(Block):
   def __init__(self, data):
      self.text = data['content']

class Random(Block):
   pass

# Expressions
class Call(Block):
   def __init__(self, data):
      print "TODO: implement call constructor"

class Decrement(Block):
   def __init__(self, data):
      self.variable = data['variable']

class Increment(Block):
   def __init__(self, data):
      self.variable = data['variable']

class Assignment(Block):
   def __init__(self, data):
      self.variable = data['variable']
      self.value = data['value']

# Text classes
class Text(Block):
   def __init__(self, data):
      self.text = data['content']

class Descriptive(Text):
   def __init__(self, data):
      pass

class Action(Text):
   def __init__(self, data):
      pass

class Narration(Text):
   def __init__(self, data):
      pass

class Speech(Text):
   def __init__(self, data):
      self.actor = data['actor']


type_map = {
      'sequence':    Sequence,
      'link':        Link,
      'decrement':   Decrement,
      'increment':   Increment,
      'assignment':  Assignment,
      'comment':     Comment,
      'action':      Action,
      'choice':      Choice,
      'conditional': Conditional,
      'call':        Call,
      'random':      Random,
      'descriptive': Descriptive,
      'narration':   Narration,
      'speech':      Speech,
      'flag':        Flag
      }

def parse_hook(data):
   if 'type' in data:
      t = data['type']
      print "Got object with type %s"%(t)
      if t in type_map:
         d = type_map[t](data)
         print d
      else:
         print "Got unknown type: %s"%(t)
   else:
      print "Got malformed data: ", data
   print
   return data

def main():
   if len(sys.argv) != 2:
      print "Usage: aucuba <json>"
      sys.exit(1)

   data = json.load(open(sys.argv[1]), object_hook=parse_hook)


if __name__ == '__main__':
   main()
