import java.util.Scanner;

class Department {
    String deptName, hodName;
    int noOfFaculty, noOfStudents, noOfPrograms;
    Department(String deptName, String hodName, int noOfFaculty, int noOfStudents, int noOfPrograms) {
        this.deptName = deptName;
        this.hodName = hodName;
        this.noOfFaculty = noOfFaculty;
        this.noOfStudents = noOfStudents;
        this.noOfPrograms = noOfPrograms;
    }
    void displayDetails() {
        System.out.println("Department: " + deptName);
        System.out.println("HOD: " + hodName);
        System.out.println("Number of Faculty: " + noOfFaculty);
        System.out.println("Number of Students: " + noOfStudents);
        System.out.println("Number of Programs: " + noOfPrograms);
    }
}
class CSE extends Department {
    CSE(String hodName, int noOfFaculty, int noOfStudents, int noOfPrograms) {
        super("CSE", hodName, noOfFaculty, noOfStudents, noOfPrograms);
    }
    @Override
    void displayDetails() {
        System.out.println("===== CSE Department =====");
        super.displayDetails();
    }
}
class AIDS extends Department {
    AIDS(String hodName, int noOfFaculty, int noOfStudents, int noOfPrograms) {
        super("AI&DS", hodName, noOfFaculty, noOfStudents, noOfPrograms);
    }
    @Override
    void displayDetails() {
        System.out.println("===== AI&DS Department =====");
        super.displayDetails();
    }
}
class CE extends Department {
    CE(String hodName, int noOfFaculty, int noOfStudents, int noOfPrograms) {
        super("CE", hodName, noOfFaculty, noOfStudents, noOfPrograms);
    }
    @Override
    void displayDetails() {
        System.out.println("===== CE Department =====");
        super.displayDetails();
    }
}
public class F3 {
    public static void main(String[] args) {
        System.out.println("Tanvik Sri Ram .R => URK23CS1261");
        Scanner sc = new Scanner(System.in);
        Department[] departments = new Department[3];
        while (true) {
            System.out.println("\nMenu:");
            System.out.println("1. Add Department Details");
            System.out.println("2. Display All Departments");
            System.out.println("3. Display Specific Department");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            int choice = sc.nextInt();
            sc.nextLine();
            switch (choice) {
                case 1:
                    System.out.println("Enter the details for 3 departments:");
                    for (int i = 0; i < 3; i++) {
                        System.out.println("Enter details for Department " + (i + 1) + " (CSE, AI&DS, CE):");
                        System.out.print("HOD Name: ");
                        String hodName = sc.nextLine();
                        System.out.print("Number of Faculty: ");
                        int noOfFaculty = sc.nextInt();
                        System.out.print("Number of Students: ");
                        int noOfStudents = sc.nextInt();
                        System.out.print("Number of Programs: ");
                        int noOfPrograms = sc.nextInt();
                        sc.nextLine();
                        if (i == 0) {
                            departments[i] = new CSE(hodName, noOfFaculty, noOfStudents, noOfPrograms);
                        } else if (i == 1) {
                            departments[i] = new AIDS(hodName, noOfFaculty, noOfStudents, noOfPrograms);
                        } else {
                            departments[i] = new CE(hodName, noOfFaculty, noOfStudents, noOfPrograms);
                        }
                    }
                    break;
                case 2:
                    System.out.println("\nAll Departments:");
                    for (Department dept : departments) {
                        if (dept != null) {
                            dept.displayDetails();
                            System.out.println("-------------------------");
                        }
                    }
                    break;
                case 3:
                    System.out.print("Enter department name to view details (CSE, AI&DS, CE): ");
                    String deptName = sc.nextLine();
                    boolean found = false;
                    for (Department dept : departments) {
                        if (dept != null && dept.deptName.equalsIgnoreCase(deptName)) {
                            dept.displayDetails();
                            found = true;
                            break;
                        }
                    }
                    if (!found) {
                        System.out.println("Department not found.");
                    }
                    break;
                case 4:
                    System.out.println("Exiting...");
                    sc.close();
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}
