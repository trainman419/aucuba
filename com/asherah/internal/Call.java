
package com.asherah.internal;

import com.asherah.AsherahState;

public class Call extends Block {
   private String function;
   private String[] arg_names;

   public Call(Block n, String f, String[] a) {
      super(n);
      function = f;
      arg_names = a;
   }

   public Block run(AsherahState state) {
      // TODO: implement
      return next;
   }
}
