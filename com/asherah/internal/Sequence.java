
package com.asherah.internal;

public class Sequence extends Branch {
   private String name;

   public Sequence(Block n, Block c, String nm) {
      super(n ,c);
      name = nm;
   }
}
