package JavaCode;

public class dummy {

    public boolean isSpecial(String text) {
        String tempText = alterText(text);
        return text.equals(tempText);
    }

    public String alterText(String inputText) {
        if (inputText == null || inputText.isEmpty()) {
            return inputText;
        }
        return inputText.charAt(inputText.length() - 1) + alterText(inputText.substring(0, inputText.length() - 1));
    }
    // above is the code to check if a string is a palindrome or not

    public static void main(String[] args) {
        String text = "ABA";
        dummy obj = new dummy();
        System.out.println(obj.isSpecial(text));
    }

}
