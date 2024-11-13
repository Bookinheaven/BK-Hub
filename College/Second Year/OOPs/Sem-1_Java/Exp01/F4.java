import java.util.Scanner;

public class F4 {
    public static void main(String[] args) {
        Scanner inputScanner = new Scanner(System.in);
        System.out.print("Enter marks for Physics: ");
        int physics = inputScanner.nextInt();
        System.out.print("Enter marks for Chemistry: ");
        int chemistry = inputScanner.nextInt();
        System.out.print("Enter marks for Biology: ");
        int biology = inputScanner.nextInt();
        System.out.print("Enter marks for Mathematics: ");
        int mathematics = inputScanner.nextInt();
        System.out.print("Enter marks for Computer: ");
        int computer = inputScanner.nextInt();

        int total = physics + chemistry + biology + mathematics + computer;
        double percentage = (total / 5.0);
        
        char grade;
        if (percentage >= 90) {
            grade = 'A';
        } else if (percentage >= 80) {
            grade = 'B';
        } else if (percentage >= 70) {
            grade = 'C';
        } else if (percentage >= 60) {
            grade = 'D';
        } else if (percentage >= 40) {
            grade = 'E';
        } else {
            grade = 'F';
        }
        System.out.println("Percentage: " + percentage + "%" + "\nGrade: " + grade);

        inputScanner.close();
    }
}
