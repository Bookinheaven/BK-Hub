class BinaryTree {
    public int data;
    public BinaryTree left;
    public BinaryTree right;

    public BinaryTree(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

public class _4_BinarySearchTree {
    private BinaryTree root;

    public void insert(int data) {
        root = insertRec(root, data);
    }

    private BinaryTree insertRec(BinaryTree root, int data) {
        if (root == null) {
            root = new BinaryTree(data);
            return root;
        }

        if (data < root.data) {
            root.left = insertRec(root.left, data); 
        } else if (data > root.data) {
            root.right = insertRec(root.right, data); 
        }

        return root;
    }

    public void inorderTraversal(BinaryTree root) {
        if (root != null) {
            inorderTraversal(root.left);
            System.out.print(root.data + " ");
            inorderTraversal(root.right);
        }
    }
    public void preorderTraversal(BinaryTree root) {
        if (root != null) {
            System.out.print(root.data + " ");
            inorderTraversal(root.left);
            inorderTraversal(root.right);
        }
    }
    public void postorderTraversal(BinaryTree root) {
        if (root != null) {
            inorderTraversal(root.left);
            inorderTraversal(root.right);
            System.out.print(root.data + " ");
        }
    }

    public static void main(String[] args) {
        _4_BinarySearchTree bst = new _4_BinarySearchTree();
        bst.insert(50);
        bst.insert(30);
        bst.insert(20);
        bst.insert(40);
        bst.insert(70);
        bst.insert(60);
        bst.insert(80);

        System.out.print("In-order traversal: ");
        bst.inorderTraversal(bst.root);
        System.out.print("Pre-order traversal: ");
        bst.preorderTraversal(bst.root);
        System.out.print("Pos-order traversal: ");
        bst.postorderTraversal(bst.root);

    }
}
