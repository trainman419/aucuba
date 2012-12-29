
package com.asherah;

import java.util.List;
import java.util.Map;
import java.util.Stack;

import java.util.LinkedList;
import java.util.HashMap;

import com.asherah.internal.Block;
import com.asherah.internal.Choice;
import com.asherah.internal.Random;

public class AsherahState {
   private Stack<Block> stack;
   private List<Choice> choice_stack;
   private List<Block> random_stack;
   private Map<String, AsherahValue> heap;

   public AsherahState() {
      stack = new Stack<Block>();
      choice_stack = new LinkedList<Choice>();
      random_stack = new LinkedList<Block>();
      heap = new HashMap<String, AsherahValue>();
   }

   // variable methods
   public boolean has(String name) {
      return heap.containsKey(name);
   }

   public AsherahValue get(String name) {
      return heap.get(name);
   }

   public void set(String name, AsherahValue v) {
      heap.put(name, v);
   }

   // stack methods
   public void stack_push(Block b) {
      stack.push(b);
   }

   public Block stack_pop() {
      if( stack.size() > 0 ) {
         return stack.pop();
      } else {
         return null;
      }
   }

   public void stack_clear() {
      stack.clear();
   }

   // choice_stack methods
   public void choice_push(Choice b) {
      choice_stack.add(b);
   }

   public int choice_size() {
      return choice_stack.size();
   }

   public Choice choice_get(int i) {
      return choice_stack.get(i);
   }

   public void choice_clear() {
      choice_stack.clear();
   }

   // random_stack methods
   public void random_push(Block b) {
      random_stack.add(b);
   }

   public int random_size() {
      return random_stack.size();
   }

   public Block random_get(int i) {
      return random_stack.get(i);
   }

   public void random_clear() {
      random_stack.clear();
   }
}
