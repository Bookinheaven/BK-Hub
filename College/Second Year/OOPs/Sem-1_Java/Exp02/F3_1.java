import java.util.Scanner;
public class F3_1 {
	public static void main(String[] args) {
        Scanner inputScan = new Scanner(System.in);
        System.out.println("Enter the string:");
        String input = inputScan.nextLine();
        System.out.println("Enter the char to count:");
        char targetChar = inputScan.next().charAt(0);
        inputScan.close();

        int count = cO(input.toCharArray(), targetChar);

        System.out.println("char '" + targetChar + "' occurs " + count + " times in the string.");
    }

    public static int cO(char[] array, char targetChar) {
        int count = 0;
        for (char c : array) {
            if (c == targetChar) {
                count++;
            }
        }
        return count;
    }
}
