import java.util.Scanner;

/**
 * Write a Java program to determine whether a given string is a palindrome. 
 * A palindrome is a word, phrase, or sequence that reads the same backward as forward.
 */
public class _12_PalindromeChecker {
    public static void main(String[] args) {
        Scanner sn = new Scanner(System.in);
        System.out.print("Enter a word: ");
        String word = sn.nextLine().strip().split(" ")[0];
        char finalword[] = new char[word.length()];
        int i = word.length() - 1; 
        for (char letter : word.toCharArray()){
            finalword [i] = letter;
            i--;
        }
        String result = new String(finalword);
        if (word.equalsIgnoreCase(result)) {
            System.out.println("The input is a palindrome.");
        } else {
            System.out.println("The input is not a palindrome.");
        }
        sn.close();
    }
}