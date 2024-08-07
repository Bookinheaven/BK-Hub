/*
 * Write a JAVA program to get a long paragraph of text and find out all the vowels
and replace it with special symbol a user inputted character, finally output the given
text and modified text.
 */

import java.util.Scanner;

public class F3 {
    public static void main(String[] args) {
        Scanner sn = new Scanner(System.in);
        System.out.print("Enter the text: ");
        char paragraph[] = sn.nextLine().toLowerCase().toCharArray();
        char vowels[] = "aeiou".toCharArray();
        System.out.print("Enter the char to change: ");
        char change = sn.next().charAt(0);
        StringBuffer output = new StringBuffer();
        for(char letter : paragraph ){
            boolean isVowel = false;
            for (int i = 0; i <= 4; i++){
                if (letter == vowels[i]){
                    output.append(change);
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
