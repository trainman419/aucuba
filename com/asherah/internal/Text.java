
package com.asherah.internal;

import com.asherah.AsherahState;

public class Text extends Block {
   private int resource_id;

   public Text(Block n, int res) {
      super(n);
      resource_id = res;
   }

   public Block run(AsherahState state) {
      return next;
   }

   public boolean has_output() {
      return true;
   }

   public int get_output() {
      return resource_id;
   }
}
