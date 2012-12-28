
package com.asherah.internal;

public class Increment extends Block {
   private String variable;

   public Increment(Block n, String var) {
      next = n;
      variable = var;
   }

   public Block run(AsherahState state) {
      AsherahValue v = state.get(variable);
      v = new AsherahValue(v.as_int() - 1);
      state.set(variable, v);

      return next;
   }
}
