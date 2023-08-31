public class pascals_triangle {
    
    public static int pascal_ncr(int n, int r){
        int res = 1;
        for (int i = 0; i < r; i++){
            res *= (n - i);
            res /= (i + 1);
        }
        return res;
    }

    public static void pascal_row_print(int n){
        int ans = 1;
        System.out.print(ans + " ");
        for (int i = 1; i < n; i++){
            ans  *= (n - i);
            ans /= i;
            System.out.print(ans + " ");    
        }
    }

    public static void main(String[] args) {
        int n =5;
        System.out.println("Pascal's Triangle");
        System.out.println(pascal_ncr(n, 2));
        pascal_row_print(n);
    }
}
