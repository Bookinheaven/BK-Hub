import java.util.ArrayList;
import java.util.Scanner;

class Employee {
    private String name, empId, department, designation;
    private int experience;
    private double basicPay, DA, gradePay, personalPay, iTax, professionalTax, epf;
    public Employee(String name, String empId, String department, String designation, int experience,
                    double basicPay, double DA, double gradePay, double personalPay,
                    double iTax, double professionalTax, double epf) {
        this.name = name;
        this.empId = empId;
        this.department = department;
        this.designation = designation;
        this.experience = experience;
        this.basicPay = basicPay;
        this.DA = DA;
        this.gradePay = gradePay;
        this.personalPay = personalPay;
        this.iTax = iTax;
        this.professionalTax = professionalTax;
        this.epf = epf;
    }
    public String getEmpId() { return empId; }
    public void setBasicPay(double basicPay) { this.basicPay = basicPay; }
    public void setDA(double DA) { this.DA = DA; }
    public void setGradePay(double gradePay) { this.gradePay = gradePay; }
    public void setPersonalPay(double personalPay) { this.personalPay = personalPay; }
    public void setITax(double iTax) { this.iTax = iTax; }
    public void setProfessionalTax(double professionalTax) { this.professionalTax = professionalTax; }
    public void setEPF(double epf) { this.epf = epf; }

    public void displayEmployee() {
        System.out.println("Employee ID: " + empId);
        System.out.println("Name: " + name);
        System.out.println("Department: " + department);
        System.out.println("Designation: " + designation);
        System.out.println("Experience: " + experience + " years");
        System.out.println("Basic Pay: " + basicPay);
        System.out.println("DA: " + DA);
        System.out.println("Grade Pay: " + gradePay);
        System.out.println("Personal Pay: " + personalPay);
        System.out.println("Income Tax: " + iTax);
        System.out.println("Professional Tax: " + professionalTax);
        System.out.println("EPF: " + epf);
    }
}
public class F3 {
    private static ArrayList<Employee> employees = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        System.out.println("Tanvik Sri Ram .R => URK23CS1261");
        while (true) {
            System.out.println("\n1. Add Employee");
            System.out.println("2. Edit Employee");
            System.out.println("3. Delete Employee");
            System.out.println("4. Display Employees");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            scanner.nextLine();

            switch (option) {
                case 1 -> addEmployee();
                case 2 -> editEmployee();
                case 3 -> deleteEmployee();
                case 4 -> displayEmployees();
                case 5 -> System.exit(0);
                default -> System.out.println("Invalid option!");
            }
        }
    }
    private static void addEmployee() {
        System.out.print("Enter Employee ID: ");
        String empId = scanner.nextLine();
        System.out.print("Enter Name: ");
        String name = scanner.nextLine();
        System.out.print("Enter Department: ");
        String department = scanner.nextLine();
        System.out.print("Enter Designation: ");
        String designation = scanner.nextLine();
        System.out.print("Enter Experience (years): ");
        int experience = scanner.nextInt();
        System.out.print("Enter Basic Pay: ");
        double basicPay = scanner.nextDouble();
        System.out.print("Enter DA: ");
        double DA = scanner.nextDouble();
        System.out.print("Enter Grade Pay: ");
        double gradePay = scanner.nextDouble();
        System.out.print("Enter Personal Pay: ");
        double personalPay = scanner.nextDouble();
        System.out.print("Enter Income Tax: ");
        double iTax = scanner.nextDouble();
        System.out.print("Enter Professional Tax: ");
        double professionalTax = scanner.nextDouble();
        System.out.print("Enter EPF: ");
        double epf = scanner.nextDouble();
        scanner.nextLine();

        Employee employee = new Employee(name, empId, department, designation, experience, basicPay, DA, gradePay, personalPay, iTax, professionalTax, epf);
        employees.add(employee);
        System.out.println("Employee added successfully.");
    }
    private static void editEmployee() {
        System.out.print("Enter Employee ID to edit: ");
        String empId = scanner.nextLine();
        for (Employee emp : employees) {
            if (emp.getEmpId().equals(empId)) {
                System.out.print("Enter new Basic Pay: ");
                emp.setBasicPay(scanner.nextDouble());
                System.out.print("Enter new DA: ");
                emp.setDA(scanner.nextDouble());
                System.out.print("Enter new Grade Pay: ");
                emp.setGradePay(scanner.nextDouble());
                System.out.print("Enter new Personal Pay: ");
                emp.setPersonalPay(scanner.nextDouble());
                System.out.print("Enter new Income Tax: ");
                emp.setITax(scanner.nextDouble());
                System.out.print("Enter new Professional Tax: ");
                emp.setProfessionalTax(scanner.nextDouble());
                System.out.print("Enter new EPF: ");
                emp.setEPF(scanner.nextDouble());
                scanner.nextLine();  // Consume newline
                System.out.println("Employee details updated.");
                return;
            }
        }
        System.out.println("Employee not found.");
    }
    private static void deleteEmployee() {
        System.out.print("Enter Employee ID to delete: ");
        String empId = scanner.nextLine();
        employees.removeIf(emp -> emp.getEmpId().equals(empId));
        System.out.println("Employee deleted successfully.");
    }
    private static void displayEmployees() {
        if (employees.isEmpty()) {
            System.out.println("No employees to display.");
        } else {
            for (Employee emp : employees) {
                emp.displayEmployee();
                System.out.println("-----------------------------");
            }
        }
    }
}
