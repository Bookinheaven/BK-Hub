"""
Python Program to Check Armstrong Number
"""

def check(num):
    sum = 0
    temp = num
    num_digits = len(str(num))
    
    while temp > 0:
        digit = temp % 10
        sum += digit ** num_digits
        temp //= 10
        print(temp)

    if sum == num:
        return 0
    else:
        return 1

num = int(input("Enter the number: "))
if check(num) == 0:
    print("It is armstrong number")
else: 
    print("its not a armstrong number")
