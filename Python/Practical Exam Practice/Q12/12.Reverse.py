"""
Given an integer number as input, display its digits in reverse order
Input : 857
Output: 758
"""
num = 857
list1 = [x for x in str(num)][::-1]
print("".join(list1))