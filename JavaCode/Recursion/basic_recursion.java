public class basic_recursion {
    // print name 5 times
    public static void print_name5(int n){
        // Base Case
        if (n == 0){
            return;
        }
        System.out.println("Mitesh");
        print_name5(n - 1);
    }

    public static void prinit_name_backtrack(int n,int count){
        if(n > count){
            return;
        }
        prinit_name_backtrack(n+1,count);
        System.out.println("Mitesh");
    }
    

    public static void print_number(int n, int count){
        //  Base Case
        if (n==0){
            return;
        }
        System.out.println(n);
        print_number(n-1,count);
    }

    public static void print_number_backtrack(int n, int count){
        // Base Case for the Backtrack
        if (n> count){
            return;
        }
        print_number_backtrack(n+1, count);
        System.out.println(n);
    }

    public static void main(String[] args) {
        System.out.println("This is printing name with recursion");
        print_name5(5);
        System.out.println("This is printing name with recursion Using Backtrack");
        prinit_name_backtrack(1, 3);
        System.out.println("This is printing number with recursion");
        print_number(5, 1);
        System.out.println("This is printing number with recursion Using Backtrack");
        print_number_backtrack(1, 5);
    }
}
