public class search {
    public static void search_in_mat_max(int[][] mat, int n, int m){
        int max = mat[0][0];
        for(int i = 0; i < n; i++){
            for(int j = 0; j<m; j++){
                max = Math.max(max, mat[i][j]);
            }
        }
        System.out.println(max + " Maximum Using brute force");
    }

    public static void search_in_mat_min(int[][] mat, int n, int m){
        int min = mat[0][0];
        for(int i = 0; i < n; i++){
            for(int j = 0; j<m; j++){
                min = Math.min(min, mat[i][j]);
            }
        }
        System.out.println(min + " Minimum Using brute force");
    }

    public static void search_element_from_mat(int[][] mat, int n, int m, int x){
        for(int i = 0; i < n; i++){
            for(int j=0; j<m; j++){
                if (mat[i][j] == x){
                    System.out.println("Element found at " + i + " " + j);
                    return;
                }
            }
        }
        System.out.println("Element not found");
    }

    public static void search_using_binary_search(int[][] mat, int n, int m, int x){
        int low = 0;
        int high = mat.length - 1;
        int mid = 0;
        //  find the row
        while(low<=high){
            mid = (low + high)/2;
            if (mat[mid][0] <= x && mat[mid][m-1] >= x){
                break;
            }
            else if (mat[mid][0] > x){
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
        }

        // find the element
        low = 0;
        high = mat[0].length - 1;
        while(low<=high){
            int mid2 = (low + high)/2;
            if (mat[mid][mid2] == x){
                System.out.println("Element found at " + mid + " " + mid2);
                return;
            }
            else if (mat[mid][mid2] > x){
                high = mid2 - 1;
            }
            else{
                low = mid2 + 1;
            }
        }   

    }

    public static void main(String[] args) {
        int[][] mat = {{1,2,3}, {4,5,6}, {7,8,9}};
        search_in_mat_max(mat, mat.length, mat[0].length);
        search_in_mat_min(mat, mat.length, mat[0].length);
        search_element_from_mat(mat, mat.length, mat[0].length, 5);
        search_using_binary_search(mat, mat.length, mat[0].length, 5);
    }
}
