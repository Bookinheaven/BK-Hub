class Account:
    def __init__(self, account_number, holder_name, balance=0.00):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Account Balance for {self.holder_name}: {self.balance}")
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account for {account.holder_name} added to the bank.")

    def view_accounts(self):
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Holder: {account.holder_name}")

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        print("Account not found.")
        return None


if __name__ == "__main__":
    my_bank = Bank()

    acc1 = Account("001", "Alice")
    acc2 = Account("002", "Bob", 1000.0)

    my_bank.add_account(acc1)
    my_bank.add_account(acc2)

    print("\nAll accounts in the bank:")
    my_bank.view_accounts()

    acc1.deposit(500.0)
    acc2.withdraw(200.0)

    acc1.check_balance()
    acc2.check_balance()

    acc_found = my_bank.get_account("002")
    if acc_found:
        print("\nAccount details:")
        print(f"Account Number: {acc_found.account_number}")
        print(f"Holder: {acc_found.holder_name}")
        print(f"Balance: {acc_found.balance}")