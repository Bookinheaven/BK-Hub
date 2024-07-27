import java.util.Scanner;
import java.util.Arrays;

public class _6_Arrays {
    public static void main(String[] args) { 
        int[] numbers = {1, 2, 3, 4, 5};
        System.out.println(numbers[0]); 
        for (int number : numbers) {
            System.out.println(number);
        }
        
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the elements: ");
        String elements[] = input.nextLine().split(" ");
        
        System.out.println(Arrays.toString(elements));
        
        input.close();
    }
    
}
