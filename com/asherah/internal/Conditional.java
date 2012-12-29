
package com.asherah.internal;

import java.util.Map;
import java.util.HashMap;

import com.asherah.AsherahState;
import com.asherah.AsherahValue;

interface Function {
   public AsherahValue call(AsherahValue args[]);
}

public class Conditional extends Branch {
   private String function;
   private String[] arg_names;
   private static Map<String, Function> functions;

   static {
      functions = new HashMap<String, Function>();

      functions.put("no", new Function() {
         public AsherahValue call(AsherahValue args[]) {
            return new AsherahValue(args[0].asInt() == 0);
         }});
      functions.put("not", new Function() {
         public AsherahValue call(AsherahValue args[]) {
            return new AsherahValue(!args[0].asBoolean());
         }});
      functions.put("use_magic", new Function() {
         public AsherahValue call(AsherahValue args[]) {
            return new AsherahValue(args[0].asBoolean());
         }});
      functions.put("", new Function() {
         public AsherahValue call(AsherahValue args[]) {
            return new AsherahValue(true);
         }});
      functions.put("with_ally", new Function() {
         public AsherahValue call(AsherahValue args[]) {
            return new AsherahValue(false);
         }});
   }

   public Conditional(Block n, Block c, String f, String [] a) {
      super(n, c);
      function = f;
      arg_names = a;

      if( ! functions.containsKey(f) ) {
         System.err.println("ERROR: unimplemented function " + f + "; " +
               "This will probably crash!!");
      }
   }

   public Block run(AsherahState state) {
      // TODO: implement conditional run
      boolean branch = false;

      if( functions.containsKey(function) ) {
         AsherahValue args[] = null;
         if( arg_names != null ) {
            args = new AsherahValue[arg_names.length];
            for( int i=0; i<arg_names.length; ++i ) {
               if( state.has(arg_names[i]) ) {
                  args[i] = state.get(arg_names[i]);
               } else {
                  args[i] = new AsherahValue(false);
                  state.set(arg_names[i], args[i]);
               }
            }
         }
         branch = functions.get(function).call(args).asBoolean();
      } else if( state.has(function) ) {
         // FIXME: hack to work around broken parser
         branch = state.get(function).asBoolean();
      } else {
         System.err.println("ERROR: tried to call undefined function " + 
               function);
      }


      if( branch ) {
         state.stack_push(next);
         return child;
      } else {
         return next;
      }
   }
}
