"""
Write a Python function to multiply all the numbers in a list.
"""

def mult(num):
    mul = 1
    for x in num:
        x = int(x)
        mul *= x
    return mul

nums = (input("Enter the numbers: ")).split()
print(f"Multiplication of {nums}: {mult(num=nums)}")
