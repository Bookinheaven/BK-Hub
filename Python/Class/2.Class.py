# class Employee:
#     def __init__(self, emp_data):
#         self.first_name = emp_data['first_name']
#         self.middle_name = emp_data['middle_name']
#         self.last_name = emp_data['last_name']
#         self.department = emp_data['department']
#         self.birth_date = emp_data['birth_date']
#         self.responsibilities = emp_data['responsibilities']
#         self.emp_id = emp_data['ID']
#         self.father_name = emp_data['father_name']
#         self.mother_name = emp_data['mother_name']
#         self.gender = emp_data['gender']

# class Manager(Employee):
#     def __init__(self, emp_data, team=None):
#         super().__init__(emp_data)
#         self.team = team if team else []    
#     def add_to_team(self,team)

# if __name__ == '__main__':
#     emp_first_name = 'Burn'
#     emp_middle_name = 'Knuckle'
#     emp_last_name = 'BK'
#     emp_department = 'CSE'
#     emp_birth_date = '24-11-2006'
#     emp_resp = 'CEO'
#     emp_id = '1261'
#     emp_father_name = 'XXXY'
#     emp_mother_name = 'YYYX'
#     emp_gender = 'M'
#     data = {
#         "first_name": emp_first_name,
#         "middle_name": emp_middle_name,
#         "last_name": emp_last_name,
#         "department": emp_department,
#         "birth_date": emp_birth_date,
#         "father_name": emp_father_name,
#         "mother_name": emp_mother_name,
#         "responsibilities": emp_resp,
#         "gender": emp_gender,
#         "ID": emp_id
#     }
#     employee = Employee(data)
#     manager = Manager(data)

class students():
    def __init__(self, name, regno):
        self.name = name
        self.regno = regno
    def setname(self, name):
        self.name = name
    def setregno(self, regno):
        self.regno = regno
    def getregno(self):
        return self.regno
    def getname(self):
        return self.name
    def __str__(self):
        return "Name: "+self.name + "\nRegno: "+ self.regno

student1 = students("David", "URK23CS8005")
print(student1)
# print("Name:", student1.getname())
# print("regno:", student1.getregno())

# student1.setname("Tanvik")
# student1.setregno("URK23CS1261")
# print("Name:", student1.getname())
# print("regno:", student1.getregno())

# student2 = students("Dinesh", "URK23CS1263")
# print("Name:", student2.getname())
# print("regno:", student2.getregno())

# student2.setname("Nivesh")
# student2.setregno("URK23CS1262")
# print("Name:", student2.getname())
# print("regno:", student2.getregno())
