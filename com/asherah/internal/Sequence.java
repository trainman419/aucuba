
package com.asherah.internal;

import com.asherah.AsherahState;

public class Sequence extends Branch {
   private String name;

   public Sequence(Block n, Block c, String nm) {
      super(n ,c);
      name = nm;
   }

   public Block run(AsherahState state) {
      if( child != null ) {
         state.stack_push(next);
         return child;
      } else {
         return next;
      }
   }

   public String toString() {
      return "com.asherah.internal.Sequence(" + name + ")";
   }
}
