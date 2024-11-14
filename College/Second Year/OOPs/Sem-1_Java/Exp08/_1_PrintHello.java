
public class _1_PrintHello {
    public static void main(String[] args) {
        createThread(1);
    }

    public static void createThread(int threadNum) {
        if (threadNum <= 50) {
            Thread thread = new Thread(() -> {
                createThread(threadNum + 1);
                System.out.println("Hello from Thread " + threadNum);
            });
            thread.start();
            try {
                thread.join();
            } catch (InterruptedException e) {
                System.err.println("Thread interrupted: " + e.getMessage());
            }
        }
    }
}
