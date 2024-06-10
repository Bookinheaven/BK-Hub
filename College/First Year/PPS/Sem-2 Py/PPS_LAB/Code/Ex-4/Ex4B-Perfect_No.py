"""
Write a python program to check whether a number is perfect or not using a function.
Note:
A positive integer is equal to the sum of its proper divisors. The smallest perfect
number is 6, which is the sum of 1, 2, and 3. Other perfect numbers are 28, 496, and 8,128."""

def is_perfect_number(number):
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i
    return divisor_sum == number

number = int(input("Enter a number: "))
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")