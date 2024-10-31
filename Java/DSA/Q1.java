public class Q1 {
    private int[] stack = null; 
    private int top = -1;
    private int size = 0;

    public Q1(int size){
        this.size = size;
        this.stack = new int[size];
    }
    private boolean isFull(){
        return this.top == this.size - 1;
    }
    private boolean isEmpty(){
        return this.top == -1;
    }
    public int peek(){
        if(!isEmpty()){
            return this.stack[this.top];
        }
        return -1;
    }
    public void push(int data){
        if (!isFull()){
            stack[++top] = data; 
            return;
        }
        System.out.println("Stack Overflow");        
    }
    public void pop(){
        if (!isEmpty()){
            stack[top--] = 0; 
            return;
        }
        System.out.println("Stack Underflow");        
    }
    public void display(){
        if (!isEmpty()){
            for (int i = 0; i <= this.top; i++){
                System.out.print(this.stack[i]+ " ");
            }
            System.err.println();
            return;
        }
        System.out.println("Empty");
    }

    public static void main(String[] args) {
        Q1 stack = new Q1(2);
        stack.push(10);
        stack.push(11);
        stack.display();
        stack.pop();
        stack.pop();
        stack.display();
        stack.pop();
    }
}