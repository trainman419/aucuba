/*
 * The core game engine for the Java implementation of Asherah
 */

package com.asherah;

import java.util.List;
import java.util.ArrayList;

public class AsherahGame<Resource> {

   /*
    * Set up the game
    */
   public AsherahGame(AsherahEngine eng, AsherahResource<Resource> res) {
      engine = eng;
      resources = res;
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
   public List<Resource> step(int choice) {
      return null;
      List<Integer> choices = engine.step(choice);
      List<Resource> result = new ArrayList<Resource>(choices.size());
      for( int i=0; i<choices.size(); ++i ) {
         result.set(i, resources.get(choices.get(i)));
      }
      return result;
   }

   private AsherahEngine engine;
   private AsherahResource<Resource> resources;
}
