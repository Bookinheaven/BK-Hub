import java.util.Scanner;

public class _7_SearchArrayPositions {
    // dont work for multiple elements with same num tho
    public static void findElementPositions(int[] mainArray, int[] searchArray) {
        for (int searchElement : searchArray) {
            boolean found = false;
            System.out.print("Positions of element " + searchElement + ": ");
            for (int i = 0; i < mainArray.length; i++) {
                if (mainArray[i] == searchElement) {
                    System.out.print(i + " "); 
                    found = true;
                }
            }
            if (!found) {
                System.out.print("Not found");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of the main array: ");
        int mainSize = sc.nextInt();
        int[] mainArray = new int[mainSize];

        System.out.println("Enter the elements of the main array:");
        for (int i = 0; i < mainSize; i++) {
            mainArray[i] = sc.nextInt();
        }

        System.out.print("Enter the size of the search array: ");
        int searchSize = sc.nextInt();
        int[] searchArray = new int[searchSize];

        System.out.println("Enter the elements of the search array:");
        for (int i = 0; i < searchSize; i++) {
            searchArray[i] = sc.nextInt();
        }

        findElementPositions(mainArray, searchArray);

        sc.close();
    }
}
