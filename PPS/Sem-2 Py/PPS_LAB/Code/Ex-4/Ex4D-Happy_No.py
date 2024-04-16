"""
4. Write a Python program to check whether a number is a Happy Number or not
Note:

A number is said to be happy if it yields 1 when replaced by the sum of squares of its
digits repeatedly. If this process results in an endless cycle of numbers containing 4, then
"""

def happy_check(num):
    str_nu = str(num)
    sum = 0
    for x in str_nu:
        sum += int(x) ** 2
    if sum == 1:
        return True
    elif sum == 4:
        return False
    else:
        return happy_check(sum)

        
check_num = int(input("Enter the no: "))
check = happy_check(check_num)
if check == True:
    print(f"{check_num} is a Happy Number")
elif check == False:
    print(f"{check_num} is not a Happy Number")
else:
    print("Error")
print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")