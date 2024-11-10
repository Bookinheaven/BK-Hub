public class _4_sieveOfEratosthenes {
    public static void main(String[] args) {
        int[] num = new int[101];
        for (int i = 1; i <= 100; i++) {
            num[i] = i;
        }
        for (int i = 2; i <= 100; i++) {
            if (num[i] != 0) { 
                for (int j = i * 2; j <= 100; j += i) {
                    num[j] = 0;
                }
            }
        }
        System.out.println("Prime numbers from 1 to 100:");
        for (int i = 2; i <= 100; i++) {
            if (num[i] != 0) {
                System.out.print(num[i] + " ");
            }
        }
    }
}
