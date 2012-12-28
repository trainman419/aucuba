
package com.asherah.internal;

import com.asherah.AsherahState;
import com.asherah.AsherahValue;

public class Assignment extends Block {
   private String variable;
   private AsherahValue value;

   public Assignment(Block n, String var, AsherahValue val) {
      super(n);
      variable = var;
      value = val;
   }

   public Block run(AsherahState state) {
      state.set(variable, value);
      return next;
   }
}
