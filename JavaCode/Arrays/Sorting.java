/**
 * Sorting
 */
import java.util.*;
public class Sorting {

    public static void bubblesort(int arr []){
        for (int turn = 0; turn< arr.length-1; turn++){
            for (int j = 0; j < arr.length - 1; j++){
                if (arr[j] > arr[j+1]){
                    int temp = arr[j+1];
                    arr[j+1] = arr[j];
                    arr[j] = temp;
                }
            }
        }
    }

    public static void selectionsort(int arr[]){
        for (int turn = 0; turn<arr.length - 1; turn++ ){
            int min_position = turn;
            for (int j = turn + 1; j< arr.length - 1; j++){
                if (arr[min_position] > arr[j]){
                    min_position = j;
                }
            }
            int temp = arr[min_position];
            arr[min_position] = arr[turn];
            arr[turn] = temp; 
        }
    }

    public static void insertionsort(int arr[]){
        for(int i= 1; i < arr.length - 1; i++){
            int curr = arr[i];
            int prev = i - 1;
            // finding the position to insert
            while (prev >= 0 && arr[prev] > curr){
                arr[prev + 1] = arr[prev];
                prev--;
            }
            // inserting the element
            arr[prev + 1] = curr;

        }
    }

    public static void countingsort(int arr[]){
        //  finding the largest element
        int largest = Integer.MIN_VALUE;
        for (int i=0; i<arr.length; i++){
            largest = Math.max(largest, arr[i]);
        }
        // creating a freq array
        int freq[] = new int[largest + 1];
        // counting the freq of each element
        for (int i=0; i<arr.length; i++){
            freq[arr[i]]++;
        }
        int j = 0;
        for (int i = 0; i<freq.length; i++){
            while(freq[i] > 0){
                arr[j] = i;
                freq[i]--;
                j++;
            }
        }



    }

    public static void main(String[] args) {
        int arr [] = {5, 4, 3, 2, 1};
        bubblesort(arr);
        System.out.println("Bubble Sort");
        printArr(arr);
        selectionsort(arr);
        System.out.println("\nSelection Sort");
        printArr(arr);
        insertionsort(arr);
        System.out.println("\nInsertion Sort");
        printArr(arr);
        countingsort(arr);
        System.out.println("\nCounting Sort");
        printArr(arr);
        
    }

    private static void printArr(int[] arr) {
        for (int i = 0; i< arr.length; i++){
            System.out.print(arr[i] + " ");
        }
    }
}