print("Ex-1 A)Write a program to find the factorial of a number using while loop\nResult:")
def factorial(num):
    fact = 1
    i = num-1
    while i > 0:
        fact *= num
        i-=1
    return fact

num = int(input("Enter the value: "))
fact = factorial(num)
print(f"Factorial: {fact}")
print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")