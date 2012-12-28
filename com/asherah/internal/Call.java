
package com.asherah.internal;

public class Call extends Block {
   private String function;
   private String[] arg_names;

   public Call(Block n, String f, String a) {
      next = n;
      function = f;
      arg_names = a;
   }

   public Block run(AsherahState state) {
      // TODO: implement
      return next;
   }
}
