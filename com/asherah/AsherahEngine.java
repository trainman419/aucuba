/*
 * The interface to the Asherah engine in Java
 *
 * Asherah programs that are compiled to Java produce a top-level class
 *  that implements this interface.
 */

package com.asherah;

import java.util.List;
import java.util.LinkedList;

public class AsherahEngine {
   private AsherahData data;

   public AsherahEngine(AsherahData d) {
      data = d;
   }

   /*
    * Get the next piece of the story
    *
    * If the list has more then one element, present them to the user as a
    *  set of choices.
    *
    * If the previous list had more than one element, choice is the index into
    *  that list of the item the user chose
    */
   public List<Integer> step(int choice) {
      List<Integer> res = new LinkedList<Integer>();
      return res;
   }

}
