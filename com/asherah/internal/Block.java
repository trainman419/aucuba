
package com.asherah.internal;

public class Block {
   private Block next;

   public Block(Block n) {
      next = n;
   }

   public Block run(AsherahState state) {
      return next;
   }
}
