
package com.asherah.internal;

import com.asherah.AsherahState;

public class Link extends Block {
   public Link() {
      super(null);
   }

   public Block run(AsherahState state) {
      state.stack_clear();
      return next;
   }

   public void setNext(Block n) {
      next = n;
   }
}
