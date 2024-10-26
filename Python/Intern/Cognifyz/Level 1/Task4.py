def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    return x % y

numberLooper : bool = True
operatorLooper : bool = True
while numberLooper:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        numberLooper = False
    except ValueError:
        print("Invalid input! Please enter numeric values.")

while operatorLooper:
    operator = input("Enter an operator (+, -, *, /, %): ")

    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    elif operator == '%':
        result = modulus(num1, num2)
    if result:
        operatorLooper = False
        print(f"The result of {num1} {operator} {num2} is: {result}")
    else:
        print("Invalid operator! Please enter one of +, -, *, /, %.")

