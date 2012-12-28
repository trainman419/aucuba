
package com.asherah.internal;

public class Random extends Branch {
   public Random(Block n, Block c) {
      next = n;
      child = c;
   }

   public Block run(AsherahState state) {
      state.random_push(child);
      return next;
   }
}
