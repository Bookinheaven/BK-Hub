/*
 * Given N numbers are entered from the keyboard into an array. The number to be
searched is entered through the keyboard by the user. Write a Java program to find if
the number to be searched is present in the array and if it is present, display the number
of times it appears in the array.
 */

import java.util.Scanner;

public class _3_NoOfElement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of elements: ");
        int length = sc.nextInt();
        int arr[] = new int[length];
        System.out.println("elements: ");
        for(int i = 0; i < length; i++){
            arr[i] = sc.nextInt();
        }
        System.out.print("Enter the number to search for: ");
        int searchNumber = sc.nextInt();
        int count = 0;
        for(int i=0; i<arr.length; i++){
            if(arr[i] == searchNumber){
                count++;
            }
        }
        System.out.println("The number " + searchNumber + " appears " + count + " times in the array.");
        sc.close();
    }
}