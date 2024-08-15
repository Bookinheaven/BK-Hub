import java.util.Scanner;

public class _9_Factorial {
    public static void main(String[] args) {
        Scanner sn = new Scanner(System.in);
        int num = sn.nextInt();
        int result = factorial(num);
        System.out.println("Factorial = " + result);
        sn.close();
    }
    // we can create a class in main method and call the method if its not static
    // because we cant call non static method from a static main method 
    public static int factorial(int num){
        return (num <= 1) ? 1 : num * factorial(num-1);
    }
    
}
