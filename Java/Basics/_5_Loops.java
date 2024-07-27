public class _5_Loops {
    public static void main(String[] args) {

        for (int i = 0; i < 5; i++) {
            System.out.println("Iteration: " + i);
        }
        int i = 0;
        while (i < 5) {
            System.out.println("Iteration: " + i);
            i++;
        }
        i = 0;
        do {
            System.out.println("Iteration: " + i);
            i++;
        } while (i < 5);
        
    }    
}
