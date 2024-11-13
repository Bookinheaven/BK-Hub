import java.util.Scanner;
/*
 * Write a java program to read the age of a candidate and determine whether he is eligible to cast his/her own vote.
 */
public class F1 {
	public static void main(String[] args) {
		Scanner inputScanner = new Scanner(System.in);
		System.out.println("Enter your age: ");
		int Age = inputScanner.nextInt();
		if (Age >= 18) {
			System.out.println("Eligible to vote");
		} else {
			System.out.println("Not Eligible to vote");	
		}
		inputScanner.close();
	}
}
