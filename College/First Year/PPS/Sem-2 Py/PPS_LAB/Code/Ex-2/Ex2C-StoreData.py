"""
Develop a Python program to input and store the provided five student details such as name, regno, cgpa as tuples in a list. Provide a menu driven option to sort the student details by name , regno and cgpa and display the appropriate sorted student details.
"""
student_data = []
for x in range(1,6):
    name = input(f"Enter The Name of Student ({x}): ")
    regno = input(f"Enter The regno of Student ({x}): ")
    cgpa = input(f"Enter The cgpa of Student ({x}): ")
    print("\n")
    student_data.append((name, regno, cgpa))
print(f"Student Data: {student_data}\n\n")
try :
    while True:
        input_sort = int(input("\tMenu: \n1.Name \n2.Regno \n3.Cgpa\n4.Exit\nSelect: "))
        if input_sort == 1:
            student_data.sort(key=lambda x: x[0]) 
            print(f"Sorted by Name: {student_data}")
        elif input_sort == 2:
            student_data.sort(key=lambda x: x[1])
            print(f"Sorted by Regno: {student_data}")
        elif input_sort == 3:
            student_data.sort(key=lambda x: float(x[2])) 
            print(f"Sorted by CGPA: {student_data}")
        elif input_sort == 4:
            exit()
except ValueError:
    print("Please enter a valid menu option.")
except Exception as e:
    print(f"Error : {e}")

print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")