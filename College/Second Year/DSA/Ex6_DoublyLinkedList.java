import java.util.Scanner;

class Node {
	Node before;
	int data;
	Node next;
	Node(Node before, int data, Node next){
		this.before = before;
		this.data = data;
		this.next = next;
	}		
}
class DoublyLinkedList{
	Node firstNode;
	Node lastNode;
	DoublyLinkedList(Node firstNode, Node lastNode){
		this.firstNode = firstNode;
		this.lastNode =lastNode;
	}
}	
public class Ex6_DoublyLinkedList {
	public static DoublyLinkedList List = new DoublyLinkedList(null, null);
	public void insertAtBeg(int data) {
		Node temp = new Node(null, data, null);
		if (List.firstNode == null) {
			List.firstNode = temp;
			List.lastNode = temp;
			return;
		}
		Node first = List.firstNode;
		first.before = temp;
		temp.next = first;
		List.firstNode = temp;
	}
	public void insertAtEnd(int data) {
		Node temp = new Node(null, data, null);
		if (List.lastNode == null) {
			List.firstNode = temp;
			List.lastNode = temp;
			return;
		}
		Node end = List.lastNode;
		end.next = temp;
		List.lastNode = temp;
	}
	public void insertAtPos(int data, int pos) {
		Node temp = new Node(null, data, null);
		if (pos == 1) {
			insertAtBeg(data);
			return;
		}
		Node posNode = List.firstNode;
		for(int i = 1; i < pos-1 && posNode != null ; i++) {
			posNode = posNode.next;
		}
		temp.next = posNode.next;
		posNode.next = temp;
	}
	public void delete(int data) {
		if (List.firstNode == null) {
            System.out.println("List is empty");
            return;
        }
        if (List.firstNode.data == data) {
        	List.firstNode = List.firstNode.next;
        	if (List.firstNode == null) {
        		List.lastNode = null;
	        }
            System.out.printf("Element %d deleted.", data);
            return;
        }
        Node temp = List.firstNode;
        while (temp != null && temp.data != data) {
            temp = temp.next;
        }
        if (temp == null) {
            System.out.printf("Element %d not found.", data);
        } else {
        	if (temp.next == null) {
	            List.lastNode = temp.before;
	        }
            temp.before.next = temp.next;
            if (temp.next != null) {
	            temp.next.before = temp.before;
	        }
            System.out.printf("Element %d deleted.", data);
        }
    }
	public void display() {
        if (List.firstNode == null) {
            System.out.println("List is empty.");
            return;
        }
        Node temp = List.firstNode;
        System.out.print("List elements: ");
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        Ex6_DoublyLinkedList list = new Ex6_DoublyLinkedList();
        while (true) {
            System.out.print("\nMenu:\n1. Add at Beginning\n2. Add at Position\n3. Add at End\n4. Delete Element\n5. Display List\n6. Exit\nEnter your choice: ");
            int choice = sc.nextInt();
            switch (choice) {
                case 1:
                    System.out.print("Enter data to insert at beginning: ");
                    int dataBeg = sc.nextInt();
                    list.insertAtBeg(dataBeg);
                    break;
                case 2:
                    System.out.print("Enter data to insert: ");
                    int dataPos = sc.nextInt();
                    System.out.print("Enter position: ");
                    int pos = sc.nextInt();
                    list.insertAtPos(dataPos, pos);
                    break;
                case 3:
                    System.out.print("Enter data to insert at end: ");
                    int dataEnd = sc.nextInt();
                    list.insertAtEnd(dataEnd);
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