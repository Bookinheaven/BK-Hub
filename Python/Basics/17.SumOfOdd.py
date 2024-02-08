
"""
Sum of odd numbers in input
"""
num = int(input("Enter the num: "))
sum = 0

for x in range(1, num+1,2):
    sum+= x


"""

for x in range(1, num+1):
    if x % 2 == 1:
        sum+= x
"""
print(f"Sum: {sum}")