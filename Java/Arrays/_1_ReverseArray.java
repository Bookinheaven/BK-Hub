/*
 * Write a Java program to reverse an array without using an additional array.
*/

import java.util.Scanner;

public class _1_ReverseArray {
    public static void main(String[] args) {
        Scanner sn = new Scanner(System.in);
        System.out.print("Enter some text using spaces: ");
        String array[] = sn.nextLine().strip().split(" ");
        int i = array.length-1;
        String output[] = new String[i+1];
        for (String y : array){
            output[i] = y;
            i--;
        }
        for (String x : output){
            System.out.printf("%s ", x);
        }
        sn.close();
    }
    // Space complexity O(n)
    // Time Complexity O(1)
}
