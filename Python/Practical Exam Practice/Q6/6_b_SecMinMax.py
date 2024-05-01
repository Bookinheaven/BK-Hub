"""
Given a list of numbers (integers), find second maximum and second minimum in this list.
Sample Input: 12 5 18 7 1 2 45 78
Output:
 Second Maximum: 45
 Second Minimum: 2
 """


num= input('Enter the numbers: ').strip().split()
maxnum = minnum = int(num[0])
sec_maxnum = sec_minnum = int(num[0])
for n in num:
    n = int(n)
    if maxnum < n:
        sec_maxnum = maxnum
        maxnum = n
    elif sec_maxnum < n and maxnum != n:
        sec_maxnum = n

    if minnum > n:
        sec_minnum = minnum
        minnum = n
    elif sec_minnum > n and minnum != n:
        sec_minnum = n 
print(f'{sec_maxnum} {sec_minnum}')

