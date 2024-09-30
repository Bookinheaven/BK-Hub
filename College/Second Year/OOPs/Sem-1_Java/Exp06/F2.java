import java.util.Scanner;

interface MathsOperable {
    double add();
    double sub();
    double mul();
    double div();
    double mod();
}

abstract class Calculator {
    double a = 0;
    double b = 0;
    double result = 0;

    Calculator(double a, double b) {
        this.a = a;
        this.b = b;
    }
}

interface TrigonometricOperable {
    double sine();
    double cosine();
    double tan();
}

class Operation extends Calculator implements TrigonometricOperable, MathsOperable {
    Operation(double a, double b) {

        super(a, b);
    }

    @Override
    public double add() {
        return a + b;
    }

    @Override
    public double sub() {
        return a - b;
    }

    @Override
    public double mul() {
        return a * b;
    }

    @Override
    public double div() {
        if (b == 0) {
            System.out.print("Div by zero error");
            return 0;
        }
        return a / b;
    }

    @Override
    public double mod() {
        return a % b;
    }

    @Override
    public double sine() {
        return Math.sin(a);
    }

    @Override
    public double cosine() {
        return Math.cos(a);
    }

    @Override
    public double tan() {
        return Math.tan(a);
    }
}

public class F2 {
    public static void main(String[] args) {
        System.out.println("Tanvik Sri Ram .R => URK23CS1261");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter value for a: ");
        double a = sc.nextDouble();
        System.out.print("Enter value for b: ");
        double b = sc.nextDouble();

        Operation operation = new Operation(a, b);

        while (true) {
            System.out.println("\nMenu:");
            System.out.println("1. Add");
            System.out.println("2. Subtract");
            System.out.println("3. Multiply");
            System.out.println("4. Divide");
            System.out.println("5. Modulus");
            System.out.println("6. Sine");
            System.out.println("7. Cosine");
            System.out.println("8. Tangent");
            System.out.println("9. Exit");
            System.out.print("Choose an option: ");
            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Result: " + operation.add());
                    break;
                case 2:
                    System.out.println("Result: " + operation.sub());
                    break;
                case 3:
                    System.out.println("Result: " + operation.mul());
                    break;
                case 4:
                    System.out.println("Result: " + operation.div());
                    break;
                case 5:
                    System.out.println("Result: " + operation.mod());
                    break;
                case 6:
                    System.out.println("Sine of a: " + operation.sine());
                    break;
                case 7:
                    System.out.println("Cosine of a: " + operation.cosine());
                    break;
                case 8:
                    System.out.println("Tangent of a: " + operation.tan());
                    break;
                case 9:
                    System.out.println("Exiting...");
                    sc.close();
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");

            }
        }
    }
}
