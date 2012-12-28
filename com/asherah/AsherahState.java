
package com.asherah;

import java.util.List;
import java.util.Map;
import java.util.Stack;

import com.asherah.internal.Block;

public class AsherahState {
   private Stack<Block> stack;
   private List<Block> choice_stack;
   private List<Block> random_stack;
   private Map<String, AsherahValue> heap;

   // variable methods
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
      return stack.pop();
   }

   public void stack_clear() {
      stack.clear();
   }

   // choice_stack methods
   public void choice_push(Block b) {
      choice_stack.add(b);
   }

   public int choice_size() {
      return choice_stack.size();
   }

   public Block choice_get(int i) {
      Block b = choice_stack.get(i);
      choice_stack.clear();
      return b;
   }


   // random_stack methods
   public void random_push(Block b) {
      random_stack.add(b);
   }

   public int random_size() {
      return random_stack.size();
   }

   public Block random_get(int i) {
      Block b = random_stack.get(i);
      random_stack.clear();
      return b;
   }
}
