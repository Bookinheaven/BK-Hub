/*
 * Write a JAVA program to get a long paragraph of text and search the given word in the text and prints out the number of times it has been occurred with its positions.

 */
import java.util.Scanner;
public class F2 {
    public static void main(String[] args) {
        Scanner sn = new Scanner(System.in);
        System.out.print("Enter the text: ");
        String paragraph[] = sn.nextLine().trim().split(" ");
        System.out.print("Enter the word to search: ");
        String Sword = sn.nextLine().trim().split(" ")[0];
        int occ = 0;
        for( String word : paragraph ){
            if (word.compareToIgnoreCase(Sword) == 0){
                occ++;
            }
        }
        System.out.print(occ);
        sn.close();
    }    
}
