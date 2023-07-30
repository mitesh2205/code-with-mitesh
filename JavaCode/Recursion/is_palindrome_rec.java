public class is_palindrome_rec {
    public static void palindrome(String str, int start, int end){
        if (start > end){
            System.out.println("Palindrome");
            return;
        }
        if (str.charAt(start) != str.charAt(end)){
            System.out.println("Not Palindrome");
            return;
        }
        palindrome(str, start + 1, end - 1);
    }

    public static void main(String[] args) {
        String str = "abbaa";
        palindrome(str, 0, str.length() - 1);
    }
}
