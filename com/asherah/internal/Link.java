
package com.asherah.internal;

public class Link extends Block {
   public Block run(AsherahState state) {
      state.stack_clear();
      return next;
   }

   public void setNext(Block n) {
      next = n;
   }
}
