"""
Write a menu driven application to maintain the employee payroll details using
Python. Your application must contain the following functionalities. Use
constructors, getter and setter functions.

a. For each employee your application must have the details such
as name, empid, department, designation, experience, basicPay,
DA(10% BP), HRA(5%BP),EPF(5%BP), Tax(10% of BP)
Net salary= BP+DA+HRA-EPF-Tax
b. Get the employee details from user(admin)
c. In the menu give the user options to add, edit, delete or display
the employee details.
"""

class Employee:
    def __init__(self):
        self.name = None
        self.empid = None
        self.department = None
        self.designation = None
        self.experience = None
        self.basicPay = None
        self.da = None
        self.hra = None
        self.epf = None
        self.Tax = None
        self.NetSalary = None

    def other_data(self, basicPay):
        try:
            self.da = 10 / 100 * basicPay
            self.hra = 5 / 100 * basicPay
            self.epf = 5 / 100 * basicPay
            self.Tax = 10 / 100 * basicPay
            self.NetSalary = basicPay + self.da + self.hra - self.epf - self.Tax
        except Exception as e:
            print(f"Error in Em __dataset : {e}")

    def set_data(self):
        self.name = input("name: ")
        self.empid = int(input("empid: "))
        self.department = input("department: ")
        self.designation = input("designation: ")
        self.experience = float(input("experience: "))
        self.basicPay = float(input("basicPay: "))

    def display(self):
        self.other_data(self.basicPay)
        print(f"""
        Employee Name: {self.name}
        Employee ID: {self.empid}
        Department: {self.department}
        Designation: {self.designation}
        Experience: {self.experience}
        Basic pay: {self.basicPay}
        DA: {self.da}
        HRA: {self.hra}
        EPF: {self.epf}
        Tax: {self.Tax}
        Net Salary: {self.NetSalary}
        """)

Emp = []

while True:
    print("""Menu:
1. Add
2. Edit
3. Delete
4. Display
5. Exit""")
    option = int(input("Enter your choice: "))
    if option == 1:
        print("Enter the new employee details: ")
        emp = Employee()
        emp.set_data()
        Emp.append(emp)
        print("Employee successfully added!")
    elif option == 2:
        empid = int(input("Enter the employee empid: "))
        found = False
        for emp in Emp:
            if emp.empid == empid:
                emp.set_data()
                found = True
                print("Employee successfully Edited!")
                break
        if not found:
            print("ID not found")
    elif option == 3:
        empid = int(input("Enter the employee empid: "))
        for emp in Emp:
            if emp.empid == empid:
                Emp.remove(emp)
                print("Employee successfully Deleted!")
                break
        else:
            print("ID not found")
    elif option == 4:
        empid = int(input("Enter the employee empid: "))
        for emp in Emp:
            if emp.empid == empid:
                emp.display()
                break
        else:
            print("ID not found")
    elif option == 5:
        quit()
