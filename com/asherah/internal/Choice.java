
package com.asherah.internal;

public class Choice extends Branch {
   private int resource_id;

   public Choice(Block n, Block c, int r) {
      next = n;
      child = c;
      resource_id = r;
   }

   public Block run(AsherahState state) {
      // TODO: push child on choice_stack
      // TODO: send resource_id to output
      return next;
   }
}
