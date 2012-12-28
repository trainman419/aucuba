
package com.asherah.internal;

import com.asherah.AsherahState;

public class Text extends Block {
   private int resource_id;

   public Text(Block n, int res) {
      super(n);
      resource_id = res;
   }

   public Block run(AsherahState state) {
      // TODO: figure out how to pass resource_id
      //  to the output layer
      return next;
   }
}
