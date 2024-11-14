import java.util.Scanner;

class CircularQueue {
    private int[] queue;
    private int rear = -1;
    private int front = -1;
    private int size;

    public CircularQueue(int size) {
        this.queue = new int[size];
        this.size = size;
    }

    public boolean isEmpty() {
        return front == -1;
    }

    public boolean isFull() {
        return (rear + 1) % size == front;
    }

    public void enqueue(int data) {
        if (!isFull()) {
            if (front == -1) {
                front = 0;
            }
            rear = (rear + 1) % size;
            queue[rear] = data;
            System.out.printf("%d enqueued\n", data);
        } else {
            System.out.println("Queue is full");
        }
    }

    public void dequeue() {
        if (!isEmpty()) {
            int value = queue[front];
            queue[front] = 0;
            if (front == rear) {
                front = rear = -1;
            } else {
                front = (front + 1) % size;
            }
            System.out.printf("%d dequeued\n", value);
        } else {
            System.out.println("Queue is empty");
        }
    }

    public void display() {
        if (isEmpty()) {
            System.out.println("Queue is empty");
        } else {
            System.out.print("Queue: [ ");
            int i = front;
            while (true) {
                System.out.print(queue[i] + " ");
                if (i == rear) {
                    break;
                }
                i = (i + 1) % size;
            }
            System.out.println("]");
        }
    }
}

public class Ex4_CircularQueue {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the circular queue: ");
        int size = scanner.nextInt();
        CircularQueue cq = new CircularQueue(size);

        while (true) {
            System.out.println("\nMenu:\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter the value to enqueue: ");
                    int data = scanner.nextInt();
                    cq.enqueue(data);
                    break;
                case 2:
                    cq.dequeue();
                    break;
                case 3:
                    cq.display();
                    break;
                case 4:
                    System.out.println("Exiting...");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        }
    }
}
