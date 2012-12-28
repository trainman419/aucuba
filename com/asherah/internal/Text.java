
package com.asherah.internal;

public class Text extends Block {
   private int resource_id;

   public Text(Block n, int res) {
      next = n;
      resource_id = res;
   }

   public Block run(AsherahState state) {
      // TODO: figure out how to pass resource_id
      //  to the output layer
      return next;
   }
