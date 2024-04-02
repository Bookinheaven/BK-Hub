class Worker:
    def __init__(self, name, salary_rate):
        self.name = name
        self.salary_rate = salary_rate
class DailyWorker(Worker):
    def comp_pay(self, days):
        return self.salary_rate * days
class SalariedWorker(Worker):
    def comp_pay(self):
        return self.salary_rate * 40
    
while True:
    print('Menu:\n1.Daily Worker\n2.Salaried Worker')
    option = int(input("Enter the option: "))
    if option == 1:
        print('Daily Worker')
        name = input("Enter the name: ")
        salar = float(input("Enter Salary Rate: "))
        days = float(input("Enter days: "))
        value = DailyWorker(name=name, salary_rate=salar).comp_pay(days)
        print(f"Com Pay: {value}")
    elif option == 2:
        print('Salaried Worker')
        name = input("Enter the name: ")
        salar = float(input("Enter Salary Rate: "))
        value = SalariedWorker(name=name, salary_rate=salar).comp_pay()
        print(f"Com Pay: {value}\n")
    else:
        quit()