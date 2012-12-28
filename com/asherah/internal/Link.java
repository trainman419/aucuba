
package com.asherah.internal;

public class Link extends Block {
   public Block run(AsherahState state) {
      // TODO: clear stack
      return next;
   }

   public void setNext(Block n) {
      next = n;
   }
}
