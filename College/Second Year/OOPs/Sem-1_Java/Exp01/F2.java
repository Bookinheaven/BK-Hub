/*
 * Write a java program to find first 10 prime numbers from natural numbers.
 */
public class F2 {
	public static void main(String[] args) {
		primenumbers(10);
	}
	static void primenumbers(int n) {
        int count = 0;
        int num = 2;

        while (count < n) {
            if (isPrime(num)) {
                System.out.println(num);
                count++;
            }
            num++;
        }
    }
	static boolean isPrime(int num) {
		if (num <= 1) {
			return false;
		}
		for(int i = 2; i <= Math.sqrt(num); i++) {
			if(num % i == 0) {
				return false;
			}
		}
		return true;
	}
	
}
