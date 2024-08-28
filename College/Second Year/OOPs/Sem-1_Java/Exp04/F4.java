import java.util.ArrayList;
import java.util.Scanner;

class Subject {
    private String subjectName, subjectCode;
    private int mark;
    private String grade;
    public Subject(String subjectName, String subjectCode, int mark) {
        this.subjectName = subjectName;
        this.subjectCode = subjectCode;
        this.mark = mark;
        this.grade = calculateGrade(mark);
    }
    private String calculateGrade(int mark) {
        if (mark >= 90) return "A+";
        else if (mark >= 80) return "A";
        else if (mark >= 70) return "B+";
        else if (mark >= 60) return "B";
        else if (mark >= 50) return "C";
        else return "F";
    }
    public String getSubjectCode() { return subjectCode; }
    public void setMark(int mark) {
        this.mark = mark;
        this.grade = calculateGrade(mark);
    }
    public void displaySubject() {
        System.out.println("Subject Name: " + subjectName);
        System.out.println("Subject Code: " + subjectCode);
        System.out.println("Mark: " + mark);
        System.out.println("Grade: " + grade);
    }
}
class Student {
    private String name, registerNo, department, specialization;
    private int semester;
    private ArrayList<Subject> subjects;
   public Student(String name, String registerNo, String department, String specialization, int semester) {
        this.name = name;
        this.registerNo = registerNo;
        this.department = department;
        this.specialization = specialization;
        this.semester = semester;
        this.subjects = new ArrayList<>();
    }
    public void addSubject(Subject subject) {
        if (subjects.size() < 5) {
            subjects.add(subject);
        } else {
            System.out.println("Cannot add more than 5 subjects.");
        }
    }

    public void editSubject(String subjectCode, int newMark) {
        for (Subject subject : subjects) {
            if (subject.getSubjectCode().equals(subjectCode)) {
                subject.setMark(newMark);
                System.out.println("Subject mark updated.");
                return;
            }
        }
        System.out.println("Subject not found.");
    }
    public void displayStudent() {
        System.out.println("Register No: " + registerNo);
        System.out.println("Name: " + name);
        System.out.println("Department: " + department);
        System.out.println("Specialization: " + specialization);
        System.out.println("Semester: " + semester);
        for (Subject subject : subjects) {
            subject.displaySubject();
            System.out.println("-----------------------------");
        }
    }
    public String getRegisterNo() { return registerNo; }
}

public class F4 {
    private static ArrayList<Student> students = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        System.out.println("Tanvik Sri Ram .R => URK23CS1261");
        while (true) {
            System.out.println("\n1. Add Student");
            System.out.println("2. Edit Student Marks");
            System.out.println("3. Delete Student");
            System.out.println("4. Display Students");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            scanner.nextLine();  // Consume newline

            switch (option) {
                case 1 -> addStudent();
                case 2 -> editStudentMarks();
                case 3 -> deleteStudent();
                case 4 -> displayStudents();
                case 5 -> System.exit(0);
                default -> System.out.println("Invalid option!");
            }
        }
    }
    private static void addStudent() {
        System.out.print("Enter Register No: ");
        String registerNo = scanner.nextLine();
        System.out.print("Enter Name: ");
        String name = scanner.nextLine();
        System.out.print("Enter Department: ");
        String department = scanner.nextLine();
        System.out.print("Enter Specialization: ");
        String specialization = scanner.nextLine();
        System.out.print("Enter Semester: ");
        int semester = scanner.nextInt();
        scanner.nextLine();  // Consume newline

        Student student = new Student(name, registerNo, department, specialization, semester);

        for (int i = 0; i < 5; i++) {
            System.out.print("Enter Subject Name: ");
            String subjectName = scanner.nextLine();
            System.out.print("Enter Subject Code: ");
            String subjectCode = scanner.nextLine();
            System.out.print("Enter Mark: ");
            int mark = scanner.nextInt();
            scanner.nextLine();  // Consume newline
            student.addSubject(new Subject(subjectName, subjectCode, mark));
        }

        students.add(student);
        System.out.println("Student added successfully.");
    }
    private static void editStudentMarks() {
        System.out.print("Enter Register No of the student: ");
        String registerNo = scanner.nextLine();
        for (Student student : students) {
            if (student.getRegisterNo().equals(registerNo)) {
                System.out.print("Enter Subject Code to edit: ");
                String subjectCode = scanner.nextLine();
                System.out.print("Enter new mark: ");
                int newMark = scanner.nextInt();
                scanner.nextLine();  // Consume newline
                student.editSubject(subjectCode, newMark);
                return;
            }
        }
        System.out.println("Student not found.");
    }
    private static void deleteStudent() {
        System.out.print("Enter Register No of the student to delete: ");
        String registerNo = scanner.nextLine();
        students.removeIf(student -> student.getRegisterNo().equals(registerNo));
        System.out.println("Student deleted successfully.");
    }
    private static void displayStudents() {
        if (students.isEmpty()) {
            System.out.println("No students to display.");
        } else {
            for (Student student : students) {
                student.displayStudent();
                System.out.println("-----------------------------");
            }
        }
    }
}
