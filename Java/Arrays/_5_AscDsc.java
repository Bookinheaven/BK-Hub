/*
 * Write a java program to copy the given N numbers of one array into another 2 arrays in
such a way that one array must contain the numbers in ascending order and the other
must contain in the descending order.
 */
import java.util.Arrays;
import java.util.Scanner;

public class _5_AscDsc {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of elements: ");
        int length = sc.nextInt();
        int ascArr[] = new int[length];
        int dscArr[] = new int[length];
        System.out.println("elements: ");
        int z = length-1;
        for(int i = 0; i < length; i++){
            int no = sc.nextInt();
            ascArr[i] = no;
            dscArr[z--] = no;

        }
        System.out.println("Ascending Array: "+ Arrays.toString(ascArr));
        System.out.println("Descending Array: "+ Arrays.toString(dscArr));
        sc.close();
    }
}