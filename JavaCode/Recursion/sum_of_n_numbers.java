public class sum_of_n_numbers {
    public static int sum_of_first_nnumbers(int n){
        // if (n == 0){
        //     System.out.println(sum);
        //     return;
        // }
        // sum_of_first_nnumbers(n-1, sum+n);

        if (n == 0 ){
            return 0;
        }
        
        return n + sum_of_first_nnumbers(n-1);


    }

    public static void main(String[] args) {
        System.out.println(sum_of_first_nnumbers(5));
    }
}
