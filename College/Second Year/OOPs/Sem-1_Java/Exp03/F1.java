/*
Write a JAVA program that asks the user to input 5 sequences of characters. Then it will ask the user for a character to search for and will output the maximum number of times that it occurred between the 5 sequences.
Example:
Sequence 1: aabc
Sequence 2: aaaa
If the user chooses to search for character 'a', the program will output "Character a
occurred a maximum of 4 times" because it occurred 4 timesin the second sequence,
and only twice in the first sequence.
*/
import java.util.Scanner;

public class F1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] sequences = new String[5];
        for (int i = 0; i < 5; i++) {
            System.out.print("Enter sequence " + (i + 1) + ": ");
            sequences[i] = scanner.nextLine();
        }

        System.out.print("Enter the character to search for: ");
        char searchChar = scanner.nextLine().charAt(0);
        int maxCount = 0;
        for (String sequence : sequences) {
            int count = 0;
            for (char ch : sequence.toCharArray()) {
                if (ch == searchChar) {
                    count++;
                }
            }
            if (count > maxCount) {
                maxCount = count;
            }
        }
        System.out.println("Character " + searchChar + " occurred a maximum of " + maxCount + " times.");
        scanner.close();
    }
}
