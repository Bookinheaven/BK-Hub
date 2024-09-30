package pk2;

import pk1.Account;

public class CurrentAccount extends Account {
    private double overdraftLimit;

    public CurrentAccount(String accountNumber, double initialBalance, double overdraftLimit) {
        super(accountNumber, initialBalance);
        this.overdraftLimit = overdraftLimit;
    }

    @Override
    public void withdraw(double amount) {
        if (amount > 0 && balance - amount >= -overdraftLimit) {
            balance -= amount;
            System.out.println("Withdrawn: " + amount);
        } else {
            System.out.println("Withdraw amount exceeds overdraft limit!");
        }
    }
}
