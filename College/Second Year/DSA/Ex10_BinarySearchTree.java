import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Ex10_BinarySearchTree {
    class Node {
        int data;
        Node left, right;
        Node(int data) {
            this.data = data;
            left = right = null;
        }
    }
    Node root;
    void insert(int data) {
        root = insertRec(root, data);
    }
    private Node insertRec(Node root, int data) {
        if (root == null)
            return new Node(data);
        if (data < root.data)
            root.left = insertRec(root.left, data);
        else if (data > root.data)
            root.right = insertRec(root.right, data);
        return root;
    }
    void inOrder(Node root) {
        if (root != null) {
            inOrder(root.left);
            System.out.print(root.data + " ");
            inOrder(root.right);
        }
    }
    void preOrder(Node root) {
        if (root != null) {
            System.out.print(root.data + " ");
            preOrder(root.left);
            preOrder(root.right);
        }
    }
    void postOrder(Node root) {
        if (root != null) {
            postOrder(root.left);
            postOrder(root.right);
            System.out.print(root.data + " ");
        }
    }
    void levelOrder(Node root) {
        if (root == null)
            return;
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            Node temp = queue.poll();
            System.out.print(temp.data + " ");
            if (temp.left != null)
                queue.add(temp.left);
            if (temp.right != null)
                queue.add(temp.right);
        }
    }
    public static void main(String[] args) {
        System.out.println("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝");
        Scanner scanner = new Scanner(System.in);
        Ex10_BinarySearchTree bst = new Ex10_BinarySearchTree();
        boolean exit = false;
        while (!exit) {
            System.out.println("\nMenu:\n1. Insert elements into the BST\n2. Display In-order traversal\n3. Display Pre-order traversal\n4. Display Post-order traversal\n5. Display Level-order traversal\n6. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    System.out.print("Enter the number of elements to insert in the BST: ");
                    int size = scanner.nextInt();
                    System.out.println("Enter the elements to insert into the BST:");
                    for (int i = 0; i < size; i++) {
                        int value = scanner.nextInt();
                        bst.insert(value);
                    }
                    System.out.println("Elements inserted successfully.");
                    break;
                case 2:
                    System.out.println("In-order traversal:");
                    bst.inOrder(bst.root);
                    System.out.println();
                    break;
                case 3:
                    System.out.println("Pre-order traversal:");
                    bst.preOrder(bst.root);
                    System.out.println();
                    break;
                case 4:
                    System.out.println("Post-order traversal:");
                    bst.postOrder(bst.root);
                    System.out.println();
                    break;
                case 5:
                    System.out.println("Level-order traversal:");
                    bst.levelOrder(bst.root);
                    System.out.println();
                    break;
                case 6:
                    exit = true;
                    System.out.println("Exiting the program.");
                    break;
                default:
                    System.out.println("Invalid option. Please choose again.");
                    break;
            }
        }
        scanner.close();
    }
}
