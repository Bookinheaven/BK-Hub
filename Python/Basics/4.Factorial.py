"""
Python Program to Find the Factorial of a Number
"""

def factorial(num):
    return 1 if num <=1 else num * factorial(num-1)

num = int(input("Enter the number: "))

print("Factorial =" ,factorial(num))