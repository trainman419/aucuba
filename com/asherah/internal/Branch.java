
package com.asherah.internal;

public class Branch extends Block {
   protected Block child;

   public Branch(Block n, Block c) {
      super(n);
      child = c;
   }
}
