public class shortestpath {
    
    public static float shortest_path(String direction){
        int x = 0;
        int y = 0;
        for(int i=0; i<direction.length(); i++){
            if(direction.charAt(i) == 'N'){
                y += 1;
            }
            else if(direction.charAt(i) == 'S'){
                y -= 1;
            }
            else if(direction.charAt(i) == 'E'){
                x += 1;
            }
            else if(direction.charAt(i) == 'W'){
                x -= 1;
            }
        }


    //     calculating displacement from the value of x and y obtained

        float displaceent = (float)Math.sqrt(Math.pow(x-0, 2) + Math.pow(y-0, 2));
        return displaceent;

    }

    public static void main(String[] args) {
        String direction = "WNEENESENNN";
        System.out.println(shortest_path(direction));
    }
}
