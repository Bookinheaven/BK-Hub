public class F1 {
    public static void main(String[] args) {
        int[] numbers = new int[100];
        
        for (int num = 2; num <= 100; num++) {
            numbers[num - 1] = num;
        }
        
        for (int place = 2; place <= 100; place++) {
            if (numbers[place - 1] != 0) {

            	for (int x = place * 2; x <= 100; x += place) {
                    numbers[x - 1] = 0;
                }
            }
        }
        
        System.out.println("Prime numbers");
        for (int num = 1; num <= 100; num++) {
            if (numbers[num - 1] != 0 && num != 1) {
                System.out.print(num + " ");
            }
        }
    }
}
