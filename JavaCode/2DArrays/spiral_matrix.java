public class spiral_matrix {
    public static void spiral(int[][] arr, int row_start, int row_end, int col_start, int col_end) {
        if (row_start > row_end || col_start > col_end) {
            return;
        }

        for (int i = col_start; i<=col_end; i++){
            System.out.print(arr[row_start][i] + " ");
        }
        row_start++;

        for (int i = row_start; i<=row_end; i++){
            System.out.print(arr[i][col_end] + " ");
        }
        col_end--;

        for (int i = col_end; i>= col_start; i--){
            System.out.print(arr[row_end][i] + " ");
        }
        row_end--;

        for (int i = row_end; i>= row_start; i--){
            System.out.print(arr[i][col_start] + " ");
        }
        col_start++;

        spiral(arr, row_start, row_end, col_start, col_end);
        
    }

    public static void main(String[] args) {
        int arr[][] = { { 1, 2, 3, 4}
                        , { 5, 6, 7, 8}
                        , { 9, 10, 11, 12}
                        , { 13, 14, 15, 16} };

        spiral(arr, 0, arr.length - 1, 0, arr[0].length - 1);
    }
}
