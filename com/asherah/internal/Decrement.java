
package com.asherah.internal;

import com.asherah.AsherahState;
import com.asherah.AsherahValue;

public class Decrement extends Block {
   private String variable;

   public Decrement(Block n, String var) {
      super(n);
      variable = var;
   }

   public Block run(AsherahState state) {
      AsherahValue v = state.get(variable);
      v = new AsherahValue(v.asInt() - 1);
      state.set(variable, v);

      return next;
   }
}
