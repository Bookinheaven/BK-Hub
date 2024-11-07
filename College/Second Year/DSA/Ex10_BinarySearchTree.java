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

    Node insertRec(Node root, int data) {
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
        System.out.print("Enter the number of elements to insert in the BST: ");
        int size = scanner.nextInt();
        int[] values = new int[size];
        System.out.println("Enter the elements to insert into the BST:");
        for (int i = 0; i < size; i++) {
            values[i] = scanner.nextInt();
        }
        for (int value : values)
            bst.insert(value);
        System.out.println("In-order:");
        bst.inOrder(bst.root);
        System.out.println("\nPre-order:");
        bst.preOrder(bst.root);
        System.out.println("\nPost-order:");
        bst.postOrder(bst.root);
        System.out.println("\nLevel-order:");
        bst.levelOrder(bst.root);
        scanner.close();
    }
}
