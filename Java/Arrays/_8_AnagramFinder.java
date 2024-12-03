import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class _8_AnagramFinder {

    public static void displayAnagrams(String[] words){
        Map<String, List<String>> anagramGroups = new HashMap<>();
        for (String word : words) {
            char[] charArray = word.toCharArray();
            Arrays.sort(charArray);
            String sortedWord = new String(charArray);
            if (!anagramGroups.containsKey(sortedWord)) {
                anagramGroups.put(sortedWord, new ArrayList<>());
            }
            anagramGroups.get(sortedWord).add(word);
        }

        System.out.println("Anagram groups:");
        for (List<String> anagrams : anagramGroups.values()) {
            if (anagrams.size() > 1) { 
                System.out.println(anagrams);
            }
        }
    }
    public static void main(String[] args) {
        String[] words = {"listen", "silent", "enlist", "rat", "tar", "god", "dog", "evil", "vile", "abc", "cba"};
        displayAnagrams(words);
    }    
}
