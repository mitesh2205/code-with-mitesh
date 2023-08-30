public class anagram {
    
    public static void is_anagram(String s1, String s2){
        int[] arr = new int[26];
        boolean is_ana = true;
        for(int i=0; i<s1.length(); i++){
            arr[s1.charAt(i) - 'a']++;
        }
        for(int i=0; i<s2.length(); i++){
            arr[s2.charAt(i) - 'a']--;
        }
        for(int i=0; i<26; i++){
            if(arr[i] != 0){
                is_ana = false;
            }
        }
        System.out.println(is_ana);
    }

    public static void main(String[] args) {
        String s1 = "rac";
        String s2 = "race";
        is_anagram(s1, s2);
    }
}
