public class rotate_matrix {

    public static void rotatematrix(int matrix[][]){
        int n = matrix.length;
        int l = 0;
        int r = n-1;

        while(l<r){
            int top = l;
            int bottom = r;
            for(int i = 0; i < r-l; i++){
                int top_left  = matrix[top][l+i];
                matrix[top][l+i] = matrix[bottom-i][l];
                matrix[bottom-i][l] = matrix[bottom][r-i];
                matrix[bottom][r-i] = matrix[top+i][r];
                matrix[top+i][r] = top_left;
            }
            l++;
            r--;
        }

        System.out.println("Rotated matrix is:");
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                System.out.print(matrix[i][j]+" ");
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args) {
        int matrix [][] = {{1,2,3},{4,5,6},{7,8,9}};
        rotatematrix(matrix);
    }
}
