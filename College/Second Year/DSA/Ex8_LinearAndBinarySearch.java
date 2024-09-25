import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

class LinearSearch {
    private ArrayList<Integer> array;
    public LinearSearch(ArrayList<Integer> numbers) {
        this.array = numbers;
    }
    public int search(int num) {
        for (int i = 0; i < array.size(); i++) {
            if (array.get(i) == num) {
                return i + 1;
            }
        }
        return -1;
    }
}
class BinarySearch {
    private ArrayList<Integer> array;
    public BinarySearch(ArrayList<Integer> numbers) {
        Collections.sort(numbers);
        this.array = numbers;
    }
    public int search(int num) {
        System.out.println("Sorted array: %s".formatted(Arrays.toString(this.array.toArray())));
        int first = 0;
        int last = array.size() - 1;
        while (first <= last) {
            int mid = first + (first + last) / 2;
            if (array.get(mid) == num) {
                return mid + 1; 
            } else if (array.get(mid) < num) {
                first = mid + 1;
            } else {
                last = mid - 1;
            }
        }
        return -1;
    }
}
public class Ex8_LinearAndBinarySearch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝");
        while (true) {
            System.out.print("\nSearch Methods by:\n1. Linear Search\n2. Binary Search\n3. Exit\nEnter your choice: ");
            int choice = sc.nextInt();
            if (choice == 3) break;
            System.out.print("Enter the elements (space-separated): ");
            sc.nextLine();
            String[] input = sc.nextLine().split(" ");
            ArrayList<Integer> numbers = new ArrayList<>();
            for (String s : input) {
                numbers.add(Integer.parseInt(s));
            }
            System.out.print("Enter the element to search: ");
            int element = sc.nextInt();
            int position;
            if (choice == 1) {
                LinearSearch linearSearch = new LinearSearch(numbers);
                position = linearSearch.search(element);
            } else if (choice == 2) {
                BinarySearch binarySearch = new BinarySearch(numbers);
                position = binarySearch.search(element);
            } else {
                System.out.println("Invalid choice. Please enter 1, 2, or 3.");
                continue;
            }
            if (position == -1) {
                System.out.println("Element not found!");
            } else {
                System.out.printf("Element found at position: %d%n", position);
            }
        }
        sc.close();
    }
}
