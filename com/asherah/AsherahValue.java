
package com.asherah;

public class AsherahValue {
   public AsherahValue(int i) {
      int_val = i;
      string_val = null;
      bool_val = i != 0;
      is_int = true;
   }

   public AsherahValue(String s) {
      string_val = s;
      int_val = s.length();
      bool_val = s.length() > 0;
      is_int = false;
   }

   public AsherahValue(boolean b) {
      if(b) {
         int_val = 1;
         string_val = "True";
      } else {
         int_val = 0;
         string_val = "False";
      }
      bool_val = b;
      is_int = false;
   }

   public bool asBoolean() {
      return bool_val;
   }

   public int asInt() {
      return int_val;
   }

   public String asString() {
      if(is_int) {
         return Integer.toString(int_val);
      } else {
         return string_val;
      }
   }

   private boolean bool_val;
   private int int_val;
   private String string_val;
   private boolean is_int;
}
