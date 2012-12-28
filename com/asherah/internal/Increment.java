
package com.asherah.internal;

public class Increment extends Block {
   private String variable;

   public Increment(Block n, String var) {
      next = n;
      variable = var;
   }

   public Block run(AsherahState state) {
      // TODO: implement
      return next;
   }
}
