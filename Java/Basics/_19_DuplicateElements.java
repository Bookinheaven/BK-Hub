
import java.util.HashSet;

public class _19_DuplicateElements {
    public static void removeDuplicates(String str1, String str2){
        StringBuilder result = new StringBuilder();
        HashSet<Character> set = new HashSet<>();  
        for(char c : str2.toCharArray()){
            set.add(c);
        }
        for (char ch : str1.toCharArray()) {
            if (!set.contains(ch)) {
                result.append(ch);
            }
        }
        System.out.println(result);
    }
    public static void removeDuplicatesShort(String str1, String str2) {
        for (char c : str2.toCharArray()) {
            str1 = str1.replaceAll(String.valueOf(c), "");
        }
        System.out.println(str1);
    }
    public static void main(String[] args) {
        removeDuplicates("programming", "gram");
        removeDuplicatesShort("programming", "gram");
    }    
}
