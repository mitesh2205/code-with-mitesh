import java.util.HashMap;
import java.util.Map;

public class temp {

   private Map<String, Integer> map;

   public temp() {
      map = new HashMap<>();
      map.put("foo", 1);
      map.put("bar", 3);
   }

   public int getValue(String input, int numRetries) throws Exception {
      try {
         return map.get(input);
      }
      catch (Exception e) {
         if (numRetries > 3) {
            throw e;
         }
         return getValue(input, numRetries + 1);
      }
   }

   public static void main(String[] args) {
        temp t = new temp();
        
        try {
            // System.out.println("Hello World! ----------------------");
            System.out.println(t.getValue("foo", 0));
            //  result  = 1 
            //  Explanation -- 0 retries, so getValue returns 1
            System.out.println(t.getValue("bar", 2));
            //  result  = 3
            //  Explanation -- 2 retries, so getValue returns 3
            System.out.println(t.getValue("baz", 0));
            //  result  = Exception thrown
            //  Explanation -- 0 retries, so getValue throws an exception
            System.out.println(t.getValue("fubar", 1));
            //  result  = Exception thrown
            //  Explanation -- 0 retries, so getValue throws an exception
            System.out.println("Hello World!_out ---------------------");

        }
        catch (Exception e) {
            System.out.println("Exception: " + e);
        }
   }
}
