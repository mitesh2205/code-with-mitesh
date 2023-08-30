public class compress_string {
    
    public static String compress(String str){
        String new_str = "";

        for(int i=0; i< str.length(); i++){
            Integer count = 1;
            while(i<str.length()-1 && str.charAt(i) == str.charAt(i+1)){
                count++;
                i++;
            }
            new_str += str.charAt(i); 
            if(count > 1){
                new_str += count;
            }
        }
        return new_str;
    }

    public static void main(String[] args) {
        String str = "aabc";

        System.out.println(compress(str));
    }
}
