// import java.util.ArrayList;

public class sum_of_subarray {
    // public static ArrayList<Integer> list_of_sum = new ArrayList<Integer>();

    public static void sum_ofsubarray(int number[]) {
        Integer max_sum = 0;
        Integer min_sum = +2147483647;
        for (int i = 0; i < number.length; i++) {
            int curr = number[i];
            for (int j = i + 1; j < number.length; j++) {
                curr += number[j];
                if (curr > max_sum) {
                    max_sum = curr;
                }
                if (curr < min_sum) {
                    min_sum = curr;
                }
                // list_of_sum.add(curr);
                System.out.print(curr + " ");
            }
            System.out.println();

        }
        System.out.println("Max Sum: " + max_sum);
        System.out.println("Min Sum: " + min_sum);
    }

    public static void kadanes(int numbers[]) {
        Integer curr_sum = 0;
        Integer max_sum = 0;
        for (int i = 0; i < numbers.length; i++) {
            curr_sum += numbers[i];
            if (curr_sum > max_sum) {
                max_sum = curr_sum;
            }
            if (curr_sum < 0) {
                curr_sum = 0;
            }
        }
        System.out.println("Max Sum: " + max_sum);
    }

    public static void main(String[] args) {
        int numbers[] = { 2, 3, 5, 6, 7 };
        sum_ofsubarray(numbers);
        System.out.println();
        System.out.println("Kadanes Algorithm: ");
        kadanes(numbers);
    }
}
// Time Complexity: O(n^2)
// Space Complexity: O(n^2)
// TC for Kadanes Algorithm: O(n)
// SC for Kadanes Algorithm: O(1)
