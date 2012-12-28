
package com.asherah.internal;

public class Conditional extends Branch {
   private String function;
   private String[] arg_names;

   public Conditional(Block n, Block c, String f, String [] a) {
      next = n;
      child = c;
      function = f;
      arg_names = a;
   }

   public Block run(AsherahState state) {
      // TODO: implement conditional run
   }
}
