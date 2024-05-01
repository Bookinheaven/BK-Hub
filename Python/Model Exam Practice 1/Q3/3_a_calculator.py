"""
Create a program to implement simple calculator for (+, -, //, *) operations using 4 user defined
functions.
Sample Input:
 Enter the number 1: 20
 Enter the number 2: 40
 Enter the operation: +
Output
 Result: 60
(similarly for other operators -,//, * it should work)
"""
def add(num1,num2):
    print(f"Result: {num1+num2}")
def sub(num1,num2):
    print(f"Result: {num1-num2}")
def mul(num1,num2):
    print(f"Result: {num1*num2}")
def div(num1,num2):
    print(f"Result: {num1//num2}")

num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
oper = input("Enter the operation: ")
if oper == '+':
    add(num1=num1,num2=num2)
elif oper == '-':
    sub(num1=num1,num2=num2)
elif oper == '*':
    mul(num1=num1,num2=num2)
elif oper == '/':
    div(num1=num1,num2=num2)
else:
    print('Wrong Operation!')