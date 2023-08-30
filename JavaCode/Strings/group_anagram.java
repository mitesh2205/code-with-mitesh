import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class group_anagram {
    
    public static void groupAnagrams(String[] arr) {
        HashMap<String, List<String>> map = new HashMap<>();
        
        for (String word : arr) {
            int[] charFrequency = new int[26];
            for (char c : word.toCharArray()) {
                charFrequency[c - 'a']++;
            }
            
            StringBuilder keyBuilder = new StringBuilder();
            for (int freq : charFrequency) {
                keyBuilder.append(freq);
            }
            
            String key = keyBuilder.toString();
            
            if (map.containsKey(key)) {
                map.get(key).add(word);
            } else {
                List<String> list = new ArrayList<>();
                list.add(word);
                map.put(key, list);
            }
        }
        
        System.out.println(map);
    }

    public static void main(String[] args) {
        String[] arr = {"eat", "tea", "tan", "ate", "nat", "bat"};
        groupAnagrams(arr);
    }
}
