package JavaCode.JavaBasics;

public class largest_number {

    public static int get_largest_number(int numbers[]) {
        int largest = Integer.MIN_VALUE;
        int smallest = Integer.MAX_VALUE;
        for (int i = 0; i < numbers.length; i++) {
            if (largest < numbers[i]) {
                largest = numbers[i];
            }
            if (smallest > numbers[i]) {
                smallest = numbers[i];
            }
        }
        System.out.println("smallest value is: " + smallest);
        return largest;
    }

    public static void main(String[] args) {
        int numbers[] = { 1, 5, 3, 7, 10, 12 };
        System.out.println("Largest value is : " + get_largest_number(numbers));

    }
}
