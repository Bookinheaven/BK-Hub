class Employee:
    no_of_em = 0
    raise_amount = 1.04
    def __init__(self, first, second, pay):
        Employee.no_of_em += 1
        self.first = first
        self.second = second
        self.email = first + second + "@gmail.com"
        self.pay = pay
    def fullname(self):
        return "{} {}".format(self.first ,self.second)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
emp_1 = Employee("Thor", "Hulk", 10000)
emp_2 = Employee("Hero", "Hulk", 10011)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(emp_2.fullname())
print(emp_1.pay)

emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.__dict__)

emp_1.raise_amount = 0.12
# Employee.raise_amount = 4.01

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.no_of_em)