import java.util.Scanner;
public class F3_2 {
	public static void main(String[] args) {
        Scanner inputScan = new Scanner(System.in);
        System.out.println("Enter the string:");
        String input = inputScan.nextLine();
        inputScan.close();
        char ans = hO(input.toCharArray());
        if (ans != 0) {
        	System.out.println("Char: "+ans);
        }
		else {
			System.out.println("No Char found");
		}
    }

    public static char hO(char[] array) {
    	char higOcChar = 0;
    	int higOcNum =0;
    	int index= 0;
        for (int x = 0; x < array.length; x++) {
        	int count = 0;
        	for (int y = 0; y < array.length; y++) {
        		if (array[x] == array[y]) {
        			count++;
        			index = x;
        		}
   
        	}
        	if(higOcNum < count) {
        		higOcNum = count;
        		higOcChar = array[index];
        	}	
        }
        System.out.println("char num: "+higOcNum);	
        return higOcChar;
    }
}
