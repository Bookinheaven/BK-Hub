/*
 * Write a Java program to check if a given number is a prime number. 
 * A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
 */
import java.util.Scanner;

public class _13_PrimeNumberChecker {
    private static boolean PrimeNumber(int number){
        if (number < 1){
            return false;
        } else{
            for (int x = 2; x <= Math.sqrt(number); x++){
                if (number % x == 0){
                    return false;
                }
            }
            return true;
        }
    }
    public static void main(String[] args) {
        Scanner sn = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = sn.nextInt();  
        boolean isPrime = PrimeNumber(number); 
        if (isPrime){
            System.out.printf("%d is a prime number", number);
        } else {
            System.out.printf("%d is not a prime number", number);
        }
    
        sn.close();
    }
}
