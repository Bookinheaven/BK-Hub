package Test;

import pk1.Account;
import pk2.SavingsAccount;
import pk2.CurrentAccount;

import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Tanvik Sri Ram .R => URK23CS1261");
        
        SavingsAccount savings = new SavingsAccount("SA12345", 1000, 3.5);
        CurrentAccount current = new CurrentAccount("CA54321", 5000, 1000);

        while (true) {
            System.out.println("\n===== Banking Operations Menu =====");
            System.out.println("1. Deposit to Savings Account");
            System.out.println("2. Withdraw from Savings Account");
            System.out.println("3. Balance Enquiry for Savings Account");
            System.out.println("4. Deposit to Current Account");
            System.out.println("5. Withdraw from Current Account");
            System.out.println("6. Balance Enquiry for Current Account");
            System.out.println("7. Exit");
            System.out.print("Enter your choice: ");
            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter amount to deposit to Savings Account: ");
                    double savingsDeposit = sc.nextDouble();
                    savings.deposit(savingsDeposit);
                    break;

                case 2:
                    System.out.print("Enter amount to withdraw from Savings Account: ");
                    double savingsWithdraw = sc.nextDouble();
                    savings.withdraw(savingsWithdraw);
                    break;

                case 3:
                    System.out.println("Savings Account Balance:");
                    savings.displayBalance();
                    break;

                case 4:
                    System.out.print("Enter amount to deposit to Current Account: ");
                    double currentDeposit = sc.nextDouble();
                    current.deposit(currentDeposit);
                    break;

                case 5:
                    System.out.print("Enter amount to withdraw from Current Account: ");
                    double currentWithdraw = sc.nextDouble();
                    current.withdraw(currentWithdraw);
                    break;

                case 6:
                    System.out.println("Current Account Balance:");
                    current.displayBalance();
                    break;

                case 7:
                    System.out.println("Exiting the application...");
                    sc.close();
                    return;

                default:
                    System.out.println("Invalid choice! Please try again.");
            }
        }
    }
}
