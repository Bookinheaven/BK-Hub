import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class _7_ExtractWord {
    public static void main(String[] args) {
        String myName = "Tanvik"; 
        char firstLetter = Character.toLowerCase(myName.charAt(0));
        try {
            File myFile = new File("findMyStuff.txt");
            Scanner scanner = new Scanner(myFile);
            int count = 0;
            while (scanner.hasNext()) {
                String word = scanner.next();
                char firstWordLetter = Character.toLowerCase(word.charAt(0));

                if (firstWordLetter == firstLetter) {
                    System.out.println(word);
                    count++;
                }
            }
            System.out.println("Total words starting with '" + firstLetter + "': " + count);

        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
        }
    }
}