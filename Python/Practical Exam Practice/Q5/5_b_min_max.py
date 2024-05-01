"""
Given a list of numbers, find the minimum value and maximum value of this list without
predefined function.
Sample Input : 12,4,8,10,1,2
Output: 1 12
"""

num= input('Enter the numbers: ').strip().split(',')
maxnum = minnum = int(num[0])
for n in num:
    n = int(n)
    if maxnum < n:
        maxnum = n
    if minnum > n:
        minnum = n
print(f'{maxnum} {minnum}')