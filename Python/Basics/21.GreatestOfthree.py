"""
Write a Python function to find the greatest of three numbers.
"""
def greatest_of_3(num):
    greatest = int(num[0])
    for x in num:
        if num[0] < x:
            x = int(x)
            greatest = x
    return greatest

nums = (input("Enter the numbers: ")).split()
print(f"Greatest of {nums}: {greatest_of_3(num=nums)}")
