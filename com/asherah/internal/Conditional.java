
package com.asherah.internal;

import com.asherah.AsherahState;

public class Conditional extends Branch {
   private String function;
   private String[] arg_names;

   public Conditional(Block n, Block c, String f, String [] a) {
      super(n, c);
      function = f;
      arg_names = a;
   }

   public Block run(AsherahState state) {
      // TODO: implement conditional run
      return next;
   }
}
