
package com.asherah.internal;

import com.asherah.AsherahState;

public class Choice extends Branch {
   private int resource_id;

   public Choice(Block n, Block c, int r) {
      super(n, c);
      resource_id = r;
   }

   public Block run(AsherahState state) {
      // push child on choice_stack
      state.choice_push(this);
      return next;
   }

   public int get_output() {
      return resource_id;
   }

   public Block get_child() {
      return child;
   }
}
