class Employee:
    def CalculateGrossSalary(self):
        gross_salary = self.basicsalary + (self.basicsalary * (self.dapay / 100)) + (self.basicsalary * (self.hra / 100))
        return gross_salary
    def CalculateTax(self):
        return (self.CalculateGrossSalary() * (self.tax / 100))
    def CalculateNetSalary(self):
        net_salary = self.CalculateGrossSalary() - self.CalculateTax() - self.epf
        return net_salary
    def display(self):
        self.NetSalary = self.CalculateNetSalary()
        return f"""
        Basic Salary: {self.basicsalary}
        DA Pay: {self.dapay}
        HRA: {self.hra}
        EPF: {self.epf}
        Tax: {self.tax}
        Net Salary: {self.NetSalary}
        """
class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.basicsalary = 30000
        self.dapay = 95
        self.hra = 20
        self.tax = 25
        self.epf = 3000

class Engineer(Employee):
    def __init__(self):
        super().__init__()
        self.basicsalary = 20000
        self.dapay = 80
        self.hra = 15
        self.tax = 15
        self.epf = 2000

def whom():
    print('1.Manager\n2.Engineer')
    option = int(input("Enter the choice: "))
    if option == 1:
        return Manager, 'Manager'
    elif option == 2:
        return Engineer, 'Engineer'
    else:
        print("Invalid Input") 
        quit()
while True:
    print('Menu:\n1.Calculate Gross Salary\n2.Calculate Net Salary\n3.Calculate Tax\n4.Print the Pay Details')
    option = int(input("Enter the option: "))
    if option == 1:
        obj, name = whom()
        print(f"{name} --> Gross Salary: {obj().CalculateGrossSalary()}\n")
    elif option == 2:
        obj, name = whom()
        print(f"{name} --> Net Salary: {obj().CalculateNetSalary()}\n")
    elif option == 3:
        obj, name = whom()
        print(f"{name} --> Tax: {obj().CalculateTax()}\n")
    elif option == 4:
        obj, name = whom()
        print(f"{name} --> Details: {obj().display()}\n")
    else:
        quit()