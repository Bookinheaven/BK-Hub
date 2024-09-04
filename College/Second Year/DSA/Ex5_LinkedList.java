import java.util.Scanner;

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class Ex5_LinkedList {
    Node start;

    public void addToEmpty(int data) {
        Node tmp = new Node(data);
        start = tmp;
    }

    public void addAtBeg(int data) {
        Node tmp = new Node(data);
        tmp.next = start;
        start = tmp;
    }

    public void addAtEnd(int data) {
        Node tmp = new Node(data);
        if (start == null) {
            addToEmpty(data);
            return;
        }
        Node p = start;
        while (p.next != null) {
            p = p.next;
        }
        p.next = tmp;
    }

    public void addAtPos(int data, int pos) {
        Node tmp = new Node(data);
        if (pos == 1) {
            tmp.next = start;
            start = tmp;
            return;
        }

        Node p = start;
        for (int i = 1; i < pos - 1 && p != null; i++) {
            p = p.next;
        }

        if (p == null) {
            System.out.println("Position out of bounds");
        } else {
            tmp.next = p.next;
            p.next = tmp;
        }
    }

    public void delete(int num) {
        if (start == null) {
            System.out.println("List is empty");
            return;
        }

        if (start.data == num) {
            start = start.next;
            System.out.println("Element " + num + " deleted.");
            return;
        }

        Node temp = start;
        Node old = null;
        while (temp != null && temp.data != num) {
            old = temp;
            temp = temp.next;
        }

        if (temp == null) {
            System.out.println("Element " + num + " not found.");
        } else {
            old.next = temp.next;
            System.out.println("Element " + num + " deleted.");
        }
    }

    public void display() {
        if (start == null) {
            System.out.println("List is empty.");
            return;
        }

        Node temp = start;
        System.out.print("List elements: ");
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Ex5_LinkedList list = new Ex5_LinkedList();
        System.out.println("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝");

        while (true) {
            System.out.print("\nMenu:\n1. Add at Beginning\n2. Add at Position\n3. Add at End\n4. Delete Element\n5. Display List\n6. Exit\nEnter your choice: ");
            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter data to insert at beginning: ");
                    int dataBeg = sc.nextInt();
                    list.addAtBeg(dataBeg);
                    break;

                case 2:
                    System.out.print("Enter data to insert: ");
                    int dataPos = sc.nextInt();
                    System.out.print("Enter position: ");
                    int pos = sc.nextInt();
                    list.addAtPos(dataPos, pos);
                    break;

                case 3:
                    System.out.print("Enter data to insert at end: ");
                    int dataEnd = sc.nextInt();
                    list.addAtEnd(dataEnd);
                    break;

                case 4:
                    System.out.print("Enter data to delete: ");
                    int delData = sc.nextInt();
                    list.delete(delData);
                    break;

                case 5:
                    list.display();
                    break;

                case 6:
                    System.out.println("Exiting...");
                    sc.close();
                    return;

                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}
