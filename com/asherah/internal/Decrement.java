
package com.asherah.internal;

public class Decrement extends Block {
   private String variable;

   public Decrement(Block n, String var) {
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
