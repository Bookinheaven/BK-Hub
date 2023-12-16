"""
Python Program to Find the Factorial of a Number
"""

def factorial(num):
    return 1 if num <=1 else num * factorial(num-1)

num = input("Enter the number: ")
if num.isdigit():
    print("Factorial =" ,factorial(int(num)))
else:
    print("Wrong enter the integer number!")