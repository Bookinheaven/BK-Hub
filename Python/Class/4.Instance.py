class Employee:
    
    def __init__(self, first, second, pay):
        self.first = first
        self.second = second
        self.email = first + second + "@gmail.com"
        self.pay = pay
    def fullname(self):
        return "{} {}".format(self.first ,self.second)
    
    
emp_1 = Employee("Thor", "Hulk", 10000)
emp_2 = Employee("Hero", "Hulk", 10011)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(emp_2.fullname())