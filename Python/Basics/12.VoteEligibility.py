"""
Write a python program to check the eligibility of voting in India
"""

name = str(input("Enter your name: "))
age = input("Enter your age: ")
if age.isdigit(): 
    if int(age) >= 18:
        print(f"{name}: Your eligible for voting")
    else :
        print(f"{name}: Your Not eligible for voting")
else: 
    print(f"Wrong {name} you need to enter integer for age!!")
