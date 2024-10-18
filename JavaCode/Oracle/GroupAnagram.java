import java.util.*;

public class GroupAnagram {
    public static void main(String[] args) {
        String words[] = { "eat", "tea", "tan", "ate", "nat", "bat" };
        groupAnagram(words);
    }

    public static void groupAnagram(String words[]){
        // create a hashmap
        Map<String, List<String>> map = new HashMap<>();

        // Iterate over the words
        for (String word: words){
            char[] ch = new char[26];
            for (char c: word.toCharArray()){
                ch[c-'a']++;
            }
            String key = new String(ch);
            if(!map.containsKey(key)){
                map.put(key, new ArrayList<>());
            }
            map.get(key).add(word);
        }
        System.out.println(map.values());
    }
}
