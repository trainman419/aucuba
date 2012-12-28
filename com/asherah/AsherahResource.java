/*
 * Resource retrieval interface for the Asherah engine in Java
 */

package com.asherah;

public interface AsherahResource<Resource> {
   /*
    * Get the Resource for a particular ID
    */
   public Resource get(int id);
}
