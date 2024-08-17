import java.util.Scanner;

class Stack{
    private String[] stack;
    private int max;
    private int top;
    
    Stack(int max){
        this.stack = new String[max];
        this.max = max;
        this.top = -1;
    }
    public void create(String[] array){
        int index = 0;
        for (String i : array){
            if (index < max && i != null){
                this.stack[index] = i;
                index++;
                this.top++;
            }
            else if (index == max){
                System.out.println("array is full");
                break;
            }
        }   
    }
    public void display(){
        for (String i : this.stack){
            System.out.print(i+" ");
        }
        System.out.println();
    }
    private boolean isFull(){
        return this.top == this.max-1;
    }
    public void push(String value){
        if (isFull()){
            System.out.println("Stack is full");
        } else {
            this.top += 1;
            this.stack[this.top] = value;
            System.out.printf("Pushed: %s \n", value);
        }
    }
    private boolean isEmpty(){
        return this.top == -1;
    }
    public void pop(){
        if (isEmpty()){
            System.out.println("Stack is Empty");
        } else {
            String popped = this.stack[this.top];
            this.stack[this.top] = null;
            this.top -= 1;
            System.out.printf("Popped: %s \n", popped);
        }
    }
    public void peek(){
        if (isEmpty()){
            System.out.println("Stack is Empty");
        } else {
            System.out.printf("Peek element in the stack: %s \n", this.stack[this.top]);
        }
    }
}

public class Ex1_Stack {
    
    public static void main(String[] args) {
        Scanner sn = new Scanner(System.in);
        System.out.print("Enter the max size of the stack: ");
        int Max = sn.nextInt();
        sn.nextLine();
        Stack stack = new Stack(Max);
        while (true) {
            System.out.println("\nMenu:\n1. Create Stack\n2. Push Element\n3. Pop Element\n4. Peek Element\n5. Display Stack\n6. Exit");
            System.out.print("Enter your choice: ");
            int choice = sn.nextInt();
            sn.nextLine();
            switch (choice) {
                case 1:
                    String array[] = new String[Max];
                    System.out.print("Enter some predefined elements (use spaces in btw): ");
                    String predefined[] = sn.nextLine().strip().split(" ");
                    int in = 0;
                    for (String x : predefined){
                        array[in] = x;
                        in++;
                    }
                    stack.create(array);
                    break;
                case 2:
                    System.out.print("Enter the value to push onto the stack: ");
                    String value = sn.nextLine().strip().split(" ")[0];
                    stack.push(value);
                    break;
                case 3:
                    stack.pop();
                    break;
                case 4:
                    stack.peek();
                    break;
                case 5:
                    stack.display();
                    break;
                case 6:
                    System.out.println("Exiting...");
                    sn.close();
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        }
    }    
}
