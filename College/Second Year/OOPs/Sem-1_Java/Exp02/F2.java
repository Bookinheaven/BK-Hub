import java.util.Scanner;

public class F2 {

    public static void main(String[] args) {
        Scanner inputScan = new Scanner(System.in);
        String input = inputScan.nextLine();
        inputScan.close();
        
        char[] charArray = input.toCharArray();
        
        char firstNonRepeated = findFNRC(charArray);
        
        if (firstNonRepeated != 0) {
            System.out.println("Char: : " + firstNonRepeated);
        } else {
            System.out.println("Not found.");
        } 
    }

    public static char findFNRC(char[] charArray) {
        for (int i = 0; i < charArray.length; i++) {
            boolean isRepeated = false;
            for (int j = 0; j < charArray.length; j++) {
                if (i != j && charArray[i] == charArray[j]) {
                    isRepeated = true;
                    break;
                }
            }
            if (!isRepeated) {
                return charArray[i];
            }
        }
        return 0;
    }
}
