import java.util.Scanner;

class Node {
    Node next;
    int data;
    Node(int data, Node next) {
        this.data = data;
        this.next = next;
    }
}
class Stacklinkedlist {
    Node top;
    public void push(int item) {
        Node temp = new Node(item, top);
        temp.data = item;
        temp.next = top;
        top = temp;
    }
    public int pop() {
        if (top == null) {
            System.out.println("Stack is empty.");
            return -1;
        }
        Node temp = top;
        int item = temp.data;
        top = top.next;
        return item;
    }
    public int peek() {
        if (top == null) {
            System.out.println("Stack is empty.");
            return -1;
        }
        return top.data;
    }
    public void display() {
        if (top == null) {
            System.out.println("Stack is empty.");
            return;
        }
        Node temp = top;
        System.out.print("List elements: ");
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }
}
class Queuelinkedlist {
    Node rear;
    Node front;
    public void enqueue(int item) {
        Node temp = new Node(item, null);
        if (front == null) {
            rear = front = temp;
            return;
        }
        rear.next = temp;
        rear = rear.next;
    }

    public int dequeue() {
        if (front == null) {
            System.out.println("Queue is empty.");
        } else {
            int item = front.data;
            front = front.next;
            return item;
        }
        return 0;
    }
    public void display() {
        if (front == null) {
            System.out.println("Queue is empty.");
            return;
        }
        Node temp = front;
        System.out.print("List elements: ");
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }
}
public class Ex7_Stacked_QueueLinkedList {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝");
        while (true) {
            System.out.print("\nCreate Linked List by:\n1.Stack\n2.Queue\n3.Exit\nEnter your choice: ");
            int choice = sc.nextInt();
            switch (choice) {
                case 1:
                    Stacklinkedlist stack = new Stacklinkedlist();
                    while (true) {
                        System.out.print("\nMenu:\n1.Push\n2.Pop\n3.Display\n4.Peek\n5.Exit\nEnter your choice: ");
                        int choice1 = sc.nextInt();
                        switch (choice1) {
                            case 1:
                                System.out.print("Enter Data: ");
                                int data = sc.nextInt();
                                stack.push(data);
                                break;
                            case 2:
                                stack.pop();
                                break;
                            case 3:
                                stack.display();
                                break;
                            case 4:
                                int top = stack.peek();
                                System.out.printf("Peek: %d", top);
                                break;
                            case 5:
                                System.out.println("Exiting...");
                                sc.close();
                                return;
                            default:
                                System.out.println("Invalid choice. Please try again.");
                        }
                    }
                case 2:
                    Queuelinkedlist queue = new Queuelinkedlist();
                    while (true) {
                        System.out.print("\nMenu:\n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit\nEnter your choice: ");
                        int choice1 = sc.nextInt();
                        switch (choice1) {
                            case 1:
                                System.out.print("Enter Data: ");
                                int data = sc.nextInt();
                                queue.enqueue(data);
                                break;
                            case 2:
                                queue.dequeue();
                                break;
                            case 3:
                                queue.display();
                                break;
                            case 4:
                                System.out.println("Exiting...");
                                sc.close();
                                return;
                            default:
                                System.out.println("Invalid choice. Please try again.");
                        }
                    }
            }
        }
    }
}