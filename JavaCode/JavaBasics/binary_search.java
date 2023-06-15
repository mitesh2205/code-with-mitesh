package JavaCode.JavaBasics;

public class binary_search {

    public static int binary_search_fun(int numbers[], int key) {
        int start = 0, end = numbers.length - 1;
        while (start <= end) {
            int mid = (start + end) / 2;

            if (numbers[mid] == key) {
                return mid;
            }
            if (numbers[mid] < key) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int numbers[] = { 2, 3, 4, 5, 6, 7, 8, 12, 14, 16, 20 };
        int key = 12;
        System.out.println("Index of key is:" + binary_search_fun(numbers, key));
    }
}
