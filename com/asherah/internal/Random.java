
package com.asherah.internal;

public class Random extends Branch {
   public Random(Block n, Block c) {
      next = n;
      child = c;
   }

   public Block run(AsherahState state) {
      // TODO: push child on random_stack
      return next;
   }
}
