import java.util.Scanner;

import java.util.Scanner;
public class count_lower_case {
 
    public static int count_lowercase(String s){
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i) >= 'a' && s.charAt(i) <= 'z'){
                return 1 + count_lowercase(s.substring(i+1));
            }
        }
        return 0;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        System.out.println(count_lowercase(str));
    }
}
