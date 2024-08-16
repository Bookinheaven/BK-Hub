import java.util.Scanner;

public class _14_FibonacciSeries {
    private static int[] Fibonacci(int number){
        int array[] = new int[number];
        array[0] = 0;
        if (number > 1){
            array[1] = 1;
            for (int i = 2; i < number; i++){
                array[i] = array[i-1] + array[i-2];
            }
        }
        return array;
    }
    public static void main(String[] args) {
        Scanner sn = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = sn.nextInt();  
        int array[] = Fibonacci(number);
        for( int i: array){
            System.out.printf("%d ", i);
        }
        sn.close();
    }    
}
