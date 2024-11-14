import java.util.Scanner;

class LinearQueue {
    private int[] queue;
    private int max;
    private int rear;
    private int front;

    LinearQueue(int max) {
        this.queue = new int[max];
        this.max = max;
        this.rear = -1;
        this.front = -1;
    }

    public boolean isEmpty() {
        return front == -1;
    }

    public boolean isFull() {
        return rear == max - 1;
    }

    public void create(int[] array) {
        for (int value : array) {
            if (!isFull() && value != 0) {
                enqueue(value);
            } else if (isFull()) {
                System.out.println("Queue is full");
                break;
            }
        }
    }

    public void enqueue(int data) {
        if (!isFull()) {
            if (front == -1) {
                front = 0;
            }
            queue[++rear] = data;
            System.out.printf("%d enqueued\n", data);
        } else {
            System.out.println("Queue is full");
        }
    }

    public void dequeue() {
        if (!isEmpty()) {
            int value = queue[front];
            queue[front++] = 0;
            if (front > rear) {
                rear = front = -1;
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
            System.out.print("[ ");
            for (int i = front; i <= rear; i++) {
                System.out.print(queue[i] + " ");
            }
            System.out.println("]");
        }
    }
}

public class Ex3_LinearQueue {
    public static void main(String[] args) {
        Scanner sn = new Scanner(System.in);
        System.out.print("Enter the max size of the queue: ");
        int max = sn.nextInt();
        sn.nextLine();
        LinearQueue queue = new LinearQueue(max);

        while (true) {
            System.out.println("\nMenu:\n1. Create Queue\n2. Enqueue Element\n3. Dequeue Element\n4. Display Queue\n5. Exit");
            System.out.print("Enter your choice: ");
            int choice = sn.nextInt();
            sn.nextLine();

            switch (choice) {
                case 1:
                    System.out.print("Enter some predefined elements (use spaces in between): ");
                    String[] predefined = sn.nextLine().strip().split(" ");
                    int[] array = new int[max];
                    for (int i = 0; i < predefined.length && i < max; i++) {
                        array[i] = Integer.parseInt(predefined[i]);
                    }
                    queue.create(array);
                    break;
                case 2:
                    System.out.print("Enter the value to enqueue: ");
                    int value = sn.nextInt();
                    sn.nextLine();
                    queue.enqueue(value);
                    break;
                case 3:
                    queue.dequeue();
                    break;
                case 4:
                    queue.display();
                    break;
                case 5:
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
