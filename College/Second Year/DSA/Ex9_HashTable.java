import java.util.Scanner;

class HashTable {
    class HashEntry {
        int regNumber;
        long mobileNumber;

        HashEntry(int regNumber, long mobileNumber) {
            this.regNumber = regNumber;
            this.mobileNumber = mobileNumber;
        }
    }

    private HashEntry[] table;
    private int size;

    public HashTable(int size) {
        this.size = size;
        table = new HashEntry[size];
    }

    private int hashFunction(int key) {
        return key % size; 
    }

    public void insert(int regNumber, long mobileNumber) {
        int index = hashFunction(regNumber);
        int startIndex = index;
        while (table[index] != null && table[index].regNumber != regNumber) {
            index = (index + 1) % size;
            if (index == startIndex) {
                break;
            }
        }
        table[index] = new HashEntry(regNumber, mobileNumber);
        System.out.println("Inserted successfully.");
    }

    public long search(int regNumber) {
        int index = hashFunction(regNumber);
        int startIndex = index;
        while (table[index] != null) {
            if (table[index].regNumber == regNumber) {
                return table[index].mobileNumber;
            }
            index = (index + 1) % size;
            if (index == startIndex) {
                break;
            }
        }
        return -1;
    }

    public void delete(int regNumber) {
        int index = hashFunction(regNumber);
        int startIndex = index;
        while (table[index] != null) {
            if (table[index].regNumber == regNumber) {
                table[index] = null;
                System.out.println("Deleted successfully.");
                return;
            }
            index = (index + 1) % size;
            if (index == startIndex) {
                break;
            }
        }
        System.out.println("Student not found.");
    }

    public void display() {
        for (int i = 0; i < size; i++) {
            if (table[i] != null) {
                System.out.println("Index " + i + ": [" + table[i].regNumber + ", " +
                        table[i].mobileNumber + "]");
            } else {
                System.out.println("Index " + i + ": [ ]");
            }
        }
    }
}

public class Ex9_HashTable {
    public static void main(String[] args) {
        System.out.println("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter hash table size: ");
        int size = sc.nextInt();
        HashTable hashTable = new HashTable(size);
        while (true) {
            System.out.print("\nMenu:\n1. Insert\n2. Search\n3. Delete\n4. Display\n5. Exit\nChoice: ");
            int choice = sc.nextInt();
            sc.nextLine();
            switch (choice) {
                case 1:
                    System.out.print("Enter register number: ");
                    int regNumber = sc.nextInt();
                    System.out.print("Enter mobile number: ");
                    long mobileNumber = sc.nextLong();
                    hashTable.insert(regNumber, mobileNumber);
                    break;
                case 2:
                    System.out.print("Enter register number to search: ");
                    regNumber = sc.nextInt();
                    long result = hashTable.search(regNumber);
                    if (result != -1) {
                        System.out.println("Mobile number found: " + result);
                    } else {
                        System.out.println("Register number not found.");
                    }
                    break;
                case 3:
                    System.out.print("Enter register number to delete: ");
                    regNumber = sc.nextInt();
                    hashTable.delete(regNumber);
                    break;
                case 4:
                    hashTable.display();
                    break;
                case 5:
                    System.out.println("Exiting.");
                    sc.close();
                    return;
                default:
                    System.out.println("Invalid choice.");
            }
        }
    }
}
