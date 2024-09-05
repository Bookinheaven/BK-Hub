import java.util.Scanner;

class ATM {
    private double balance;
    private String pin;
    public ATM(double initialBalance, String initialPin) {
        this.balance = initialBalance;
        this.pin = initialPin;
    }
    public double getBalance() { return balance; }
    public void setBalance(double balance) { this.balance = balance; }
    public String getPin() { return pin; }
    public void setPin(String pin) { this.pin = pin; }
    public void checkBalance() {
        System.out.println("Your current balance is: $" + balance);
    }
    public void withdraw(double amount) {
        if (amount <= 0) {
            System.out.println("Invalid amount.");
            return;
        }
        if (amount % 100 != 0) {
            System.out.println("Amount must be a multiple of 100.");
            return;
        }
        if (balance - amount <= 500) {
            System.out.println("Insufficient balance. You must maintain a minimum balance of $500.");
            return;
        }
        balance -= amount;
        System.out.println("Withdrawal successful. Amount withdrawn: $" + amount);
    }
    public void changePin(String newPin) {
        this.pin = newPin;
        System.out.println("PIN changed successfully.");
    }
}

public class F5 {
    private static ATM atm = new ATM(1000, "1234");
    private static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        System.out.println("Tanvik Sri Ram .R => URK23CS1261");
        while (true) {
            System.out.println("\n1. Balance Enquiry");
            System.out.println("2. Withdrawal");
            System.out.println("3. Change PIN");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            scanner.nextLine();  
            switch (option) {
                case 1 -> atm.checkBalance();
                case 2 -> withdrawMoney();
                case 3 -> changePin();
                case 4 -> System.exit(0);
                default -> System.out.println("Invalid option!");
            }
        }
    }
    private static void withdrawMoney() {
    System.out.print("Enter the pin: ");
    String Pin = scanner.nextLine();
    if(!Pin.equals(atm.getPin()) ) {
    System.out.println("Invalid pin!");
    return;
    }
        System.out.print("Enter amount to withdraw: ");
        double amount = scanner.nextDouble();
        scanner.nextLine();
        atm.withdraw(amount);
    }
    private static void changePin() {
        System.out.print("Enter new PIN: ");
        String newPin = scanner.nextLine();
        atm.changePin(newPin);
    }
}