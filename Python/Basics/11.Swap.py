"""
Write a Python program to swap two variables
"""

a = int(input("Enter 1nd value: "))
b = int(input("Enter 2nd value: "))

print(f"Before Swap: {a} ; {b}")
#using third variable
"""
temp = a
a = b
b = temp
#without 3rd variable
"""
a = a+b
b = a-b
a = a-b

print(f"After Swap: {a} ; {b}")
