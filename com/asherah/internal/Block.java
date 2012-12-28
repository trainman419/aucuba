
package com.asherah.internal;

import com.asherah.AsherahState;

public class Block {
   protected Block next;

   public Block(Block n) {
      next = n;
   }

   public Block run(AsherahState state) {
      return next;
   }
}
