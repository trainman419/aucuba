
import java.util.List;
import java.util.Scanner;

import com.asherah.AsherahGame;
import com.asherah.AsherahEngine;

public class Sample {
   private static void print(String s) {
      System.out.println(s);
   }

   public static void main(String args[]) {
      Complete_output data = new Complete_output();
      Complete_outputTextResource text = new Complete_outputTextResource();
      AsherahEngine eng = new AsherahEngine(data);
      AsherahGame<String> game = new AsherahGame<String>(eng, text);

      List<String> output;
      int choice = 0;

      Scanner in = new Scanner(System.in);

      do {
         output = game.step(choice);
         choice = 0;
         if( output.size() > 1 ) {
            int i = 1;
            for( String s : output ) {
               print(i + ") " + s);
               i++;
            }
            print("");
            System.out.print("> ");
            choice = in.nextInt() - 1;
         } else if( output.size() == 1) {
            print(output.get(0));
         }
      } while( output.size() > 0 );
   }
}
