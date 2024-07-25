package Ex02;

import java.util.Scanner;
public class F3_2 {
	public static void main(String[] args) {
        Scanner inputScan = new Scanner(System.in);
        System.out.println("Enter the string:");
        String input = inputScan.nextLine();
        inputScan.close();
         hO(input);

     
    }

    public static int[] hO(char[] array) {
        int[] occCounter = new int[array.length];
        for (int x = 0; x < array.length; x++) {
        	int count = 0;
        	for (int y = 0; y < array.length; j++) {
        		if (x != y && array[x] == array[y]) {
        			count++;
        		}
        	}
        	occCounter[x] = count;
        }
        
        return occCounter;
    }
}
