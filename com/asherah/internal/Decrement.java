
package com.asherah.internal;

public class Decrement extends Block {
   private String variable;

   public Decrement(Block n, String var) {
      next = n;
      variable = var;
   }

   public Block run(AsherahState state) {
      // TODO: implement
      return next;
   }
}
