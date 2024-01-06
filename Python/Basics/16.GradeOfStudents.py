"""
Write a program to calculate grade of a student for 3 subjects
"""
avg = 0
for x in range(1,4):
    marks = int(input(f"Marks of subject({x}): "))
    avg += marks
avg //= 3
if(avg >= 90 and avg <= 100):
    print("Grade: A")
elif(avg >= 60 and avg < 90):
    print("Grade: B")
else:
    print("Fail")