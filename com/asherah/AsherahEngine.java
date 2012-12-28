/*
 * The interface to the Asherah engine in Java
 *
 * Asherah programs that are compiled to Java produce a top-level class
 *  that implements this interface.
 */

package com.asherah;

import java.util.List;
import java.util.LinkedList;

import com.asherah.internal.Block;

public class AsherahEngine {
   private AsherahData data;

   private Block current;
   private AsherahState state;
   private boolean pending_choice;
   private java.util.Random rand;

   public AsherahEngine(AsherahData d) {
      data = d;
      current = d.getMain();
      state = new AsherahState();
      pending_choice = false;
      rand = new java.util.Random();
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
      if( pending_choice ) {
         current = state.choice_get(choice).get_child();
         if( current == null ) {
            current = state.stack_pop();
         }
         state.choice_clear();
         pending_choice = false;
      }
      while( current != null && ! current.has_output() ) {
         System.out.println(current);
         current = current.run(state);
         if( current == null ) {
            current = state.stack_pop();
         }
         if( current != null && current.has_output() && 
               state.random_size() > 0 ) {
            state.stack_push(current);
            int sz = state.random_size();
            current = state.random_get(rand.nextInt(sz));
            state.random_clear();
         }
      }

      if( state.choice_size() > 0 ) {
         state.stack_push(current);

         for( int i=0; i<state.choice_size(); ++i ) {
            res.add(state.choice_get(i).get_output());
         }
         pending_choice = true;
      } else {
         if( current != null ) {
            res.add(current.get_output());
            current = current.run(state);
            if( current == null ) {
               current = state.stack_pop();
            }
         }
      }
      return res;
   }

}
