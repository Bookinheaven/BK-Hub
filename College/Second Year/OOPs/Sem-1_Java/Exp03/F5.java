/*
 * Write a program to delete all vowels from a given sentence. Assume that the sentence is not more than 80 characters long.
 */

import java.util.Scanner;

public class F5 {
    public static void main(String[] args) {
        Scanner sn = new Scanner(System.in);
        System.out.print("Enter the text: ");
        String input = sn.nextLine();
        StringBuilder output = new StringBuilder(); 
        char vowels[] = "aeiou".toCharArray();
        for(char letter : input.toCharArray() ){
            boolean isVowel = false;
            for (int i = 0; i <= 4; i++){
                if (letter == vowels[i]){
                    isVowel = true;
                }
            }
            if (!isVowel){
                output.append(letter);
            }            
        }
        System.out.print("Output: "+output);
        sn.close();
    }
}
