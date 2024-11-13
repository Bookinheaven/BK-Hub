import java.util.Scanner;

public class F5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = scanner.nextInt();

        while (true) {
            System.out.println("Choose an operation:\n1. Check if the number is a Buzz number\n2. Check if the number is even or odd\n3. Check if the number is positive or negative\n4. Exit\nEnter your choice: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1 -> {
                    if (isBuzzNumber(number)) {
                        System.out.println(number + " is a Buzz number.");
                    } else {
                        System.out.println(number + " is not a Buzz number.");
                    }
                }
                case 2 -> {
                    if (isEven(number)) {
                        System.out.println(number + " is even.");
                    } else {
                        System.out.println(number + " is odd.");
                    }
                }
                case 3 -> {
                    if (isPositive(number)) {
                        System.out.println(number + " is positive.");
                    } else {
                        System.out.println(number + " is negative.");
                    }
                }
                case 4 -> {
                    System.out.println("Exiting...");
                    scanner.close();
                    return;
                }
                default -> System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    public static boolean isBuzzNumber(int num) {
        return num % 7 == 0 || num % 10 == 7;
    }

    public static boolean isEven(int num) {
        return num % 2 == 0;
    }

    public static boolean isPositive(int num) {
        return num >= 0;
    }
}
