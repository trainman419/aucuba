
package com.asherah.internal;

import com.asherah.AsherahState;

public class Random extends Branch {
   public Random(Block n, Block c) {
      super(n, c);
   }

   public Block run(AsherahState state) {
      state.random_push(child);
      return next;
   }
}
