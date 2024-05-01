"""
Develop a Python application using Inheritance as per the following. Create a class Worker with
name, salary rate as data members (use __init_ to initialize it) and derive two classes
DailyWorker and SalariedWorker from it. Provide a method ComputePay(int hours) to
compute the week pay of every worker. A DailyWorker is paid on the basis of number of days
he/she works. The SalariedWorker gets paid the wage for 40 hours a week no matter what
actual hours is. Implement this scenario to calculate the pay of workers with menu options
Menu Options
1.Salaried Worker
2.Daily Worker
If user selects 1.
Enter the name: abc
Enter the number of hours: 5 hours
Total Pay:
"""
class Worker:
    def __init__(self, name, salary_rate):
        self.name = name
        self.salary_rate = salary_rate
class DailyWorker(Worker):
    def compute_pay(self, days):
        return self.salary_rate * days
class SalariedWorker(Worker):
    def compute_pay(self, hours):
        if hours > 40:
            h = 40
        else:
            h = hours
        return self.salary_rate * h
print("Menu Options")
print("1. Salaried Worker")
print("2. Daily Worker")
choice = int(input("Enter your choice: "))

name = input("Enter the name: ")
salary_rate = float(input("Enter the salary rate: "))

if choice == 1:
    hours = int(input("Enter the number of hours: "))
    worker = SalariedWorker(name, salary_rate)
    total_pay = worker.compute_pay(hours)
elif choice == 2:
    days = int(input("Enter the number of days: "))
    worker = DailyWorker(name, salary_rate)
    total_pay = worker.compute_pay(days)
else:
    print("Invalid choice!")
    
print("Total Pay:", total_pay)