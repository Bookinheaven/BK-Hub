import java.util.Scanner;
import java.util.Stack;

public class Ex2_InfixToPostfix {
    private String expression = "";
    private final String operators = "+-/*^";
    private final Stack<Character> operatorStack;
    
    public Ex2_InfixToPostfix(String expression){
        this.expression = expression.replaceAll("\\s+", "");
        this.operatorStack = new Stack<>();
    }
    private int precedence(char operator) {
        return switch (operator) {
            case '^' -> 3;
            case '*', '/' -> 2;
            case '+', '-' -> 1;
            default -> 0;
        };
    }
    public void infixToPostfix() {
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < expression.length(); i++) {
            char current = expression.charAt(i);
            if (Character.isLetterOrDigit(current)) {
                output.append(current);
            } else if (current == '(') {
                operatorStack.push(current);
            } else if (operators.indexOf(current) != -1) {
                while (!operatorStack.isEmpty() && operatorStack.peek() != '('
                && ((precedence(operatorStack.peek()) >= precedence(current)) && current != '^')) {
                    output.append(operatorStack.pop());
                }
                operatorStack.push(current);
            } else if (current == ')') {
                while (!operatorStack.isEmpty() && operatorStack.peek() != '(') {
                    output.append(operatorStack.pop());
                }
                if (!operatorStack.isEmpty() && operatorStack.peek() == '(') {
                    operatorStack.pop();
                }
            }
        }

        while (!operatorStack.isEmpty()) {
            output.append(operatorStack.pop());
        }
        System.out.println("Postfix Expression: " + output.toString());
    }
    public void evaluatePostfix() {
        Stack<Integer> evaluationStack = new Stack<>();
        for (int i = 0; i < expression.length(); i++) {
            char current = expression.charAt(i);
            if (Character.isDigit(current)) {
                evaluationStack.push(Character.getNumericValue(current));
            } else if (operators.indexOf(current) != -1) {
                if (evaluationStack.size() < 2) {
                    System.out.println("Error: Invalid expression");
                    return;
                }
                int op1 = evaluationStack.pop();
                int op2 = evaluationStack.pop();
                switch (current) {
                    case '+' -> evaluationStack.push(op2 + op1);
                    case '-' -> evaluationStack.push(op2 - op1);
                    case '*' -> evaluationStack.push(op2 * op1);
                    case '/' -> evaluationStack.push(op2 / op1);
                    case '^' -> evaluationStack.push((int) Math.pow(op2, op1));
                }
            }
        }
        if (!evaluationStack.isEmpty()) {
            System.out.println("Postfix Expression Evaluation: " + evaluationStack.peek());
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\nMenu:\n1. Infix to Postfix\n2. Evaluate Postfix Expression\n3. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); 
            switch (choice) {
                case 1 -> {
                    System.out.print("Enter the Expression: ");
                    String expression = scanner.nextLine();
                    Ex2_InfixToPostfix instance = new Ex2_InfixToPostfix(expression);
                    instance.infixToPostfix();
                }
                case 2 -> {
                    System.out.print("Enter the Expression: ");
                    String expression = scanner.nextLine();
                    Ex2_InfixToPostfix instance = new Ex2_InfixToPostfix(expression);
                    instance.evaluatePostfix();
                }
                case 3 -> {
                    System.out.println("Exiting...");
                    System.exit(0);
                    return;
                }
                default -> System.out.println("Invalid choice. Please try again.");
            }
        }
    } 
}
