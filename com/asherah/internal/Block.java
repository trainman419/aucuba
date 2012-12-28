
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

   public boolean has_output() {
      return false;
   }

   public int get_output() {
      return -1;
   }
}
