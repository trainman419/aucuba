
package com.asherah.internal;

public class Assignment extends Block {
   private String variable;
   private AsherahValue value;

   public Assignment(Block n, String var, AsherahValue val) {
      next = n;
      variable = var;
      value = val;
   }

   public Block run(AsherahState state) {
      // TODO: implement
      return next;
   }
}
