"""
Python Program to Find Sum of Array
"""

def sum_of_arrays(arr):
    sum = 0
    for x in arr:
        sum+= x
    return sum

arr = [1,2,3,4,5,6,7,8,9,10]
print("Sum =", sum_of_arrays(arr))