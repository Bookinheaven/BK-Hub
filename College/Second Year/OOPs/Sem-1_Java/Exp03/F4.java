/*
 * Write a program that converts all lowercase characters in a given string to its equivalent uppercase character. (Note: If space comes leave it as it is).
 */

import java.util.Scanner;
import java.lang.Character;
public class F4 {
    public static void main(String[] args) {
        Scanner sn = new Scanner(System.in);
        System.out.print("Enter the text: ");
        String input = sn.nextLine();
        StringBuilder output = new StringBuilder(); 
        for( char ch : input.toCharArray()){
            if (Character.isLowerCase(ch)){
                output.append(Character.toUpperCase(ch));
            }
            else{
                output.append(ch);
            }
        }

        System.out.println("Ouput: "+output);
        sn.close();
    }
}
