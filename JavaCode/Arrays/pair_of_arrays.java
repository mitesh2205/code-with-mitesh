public class pair_of_arrays {
    public static void pair_array(int number[]) {
        for (int i = 0; i < number.length; i++) {
            int curr = number[i];
            for (int j = i + 1; j < number.length; j++) {
                System.out.print("( " + curr + ", " + number[j] + " )");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int numbers[] = { 2, 3, 5, 6, 7 };
        pair_array(numbers);
    }
}
