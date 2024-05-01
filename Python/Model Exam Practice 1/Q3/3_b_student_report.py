"""
Develop a Python program to generate reports of students with the following
specifications. Create a class called Student with attributes regno, name, cgpa, and
include necessary constructor, and accessors /mutators methods. Create two Student
objects and display their reports
"""
class Student:
    def __init__(self) -> None:
        self.regno = None
        self.name = None
        self.cgpa = None
    def display(self):
        print(f"\n-------------\nName: {self.name}\nRegno: {self.regno}\nCgpa: {self.cgpa}\n-------------")
    def change(self, what, value):
        if what == 'name':
            self.name = value
        elif what == 'regno':
            self.regno = value
        elif what == 'cgpa':
            self.cgpa = value
    def set_data(self, name, regno, cgpa):
        self.name = name
        self.regno = regno
        self.cgpa = cgpa

studentslist = []
while(True):
    print('\ntudents Report')
    menu = int(input("\nMenu\n1.Add Student Info\n2.Change Student Info\n3.Display Student Info\n4.Delete Student Info\n5.Exit\nSelect:"))
    print(f"Selected option {menu}")
    if menu == 1:
        name = input("\nEnter Student Name: ").lower()
        regno = input("Enter Student Regno: ")
        cgpa = input("Enter Student CGPA: ")
        student = Student()
        student.set_data(name=name, regno=regno, cgpa=cgpa)
        studentslist.append(student)
        print(f"Student {name} added to students list")
    elif menu == 2:
        name = input('\nEnter student name: ').lower()
        for student in studentslist:
            if student.name == name:
                while True:
                    what = int(input(f"\nWhat do you want to change in student {name} Info?\n1.Name\n2.Regno\n3.Cgpa\n4.Done\n Select: "))
                    if what == 1:
                        name = input("Enter Student Name: ").lower()
                        student.change(what='name', value=name)
                    elif what == 2:
                        regno = input("Enter Student Regno: ")
                        student.change(what='regno', value=regno)
                    elif what == 3:
                        cgpa = input("Enter Student CGPA: ") 
                        student.change(what='cgpa', value=cgpa)
                    elif what == 4:
                        print("Student Info Uploaded")
                        student.display()
                        break
            else:
                print(f"Student {name} not found in list!")
    elif menu == 3:
        name = input('\nEnter student name: ').lower()
        for student in studentslist:
            if student.name == name:
                student.display()
            else:
                print(f"Student {name} not found in list!")
    elif menu == 4:
        name = input('\nEnter student name: ').lower()
        for student in studentslist:
            if student.name == name:
                studentslist.remove(student)
                print(f"Student {name} removed from list!")
            else:
                print(f"Student {name} not found in list!")
    elif menu == 5:
        print("Exiting ")
        quit()
    
        