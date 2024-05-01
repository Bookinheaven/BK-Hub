"""
Given a list of numbers, find and print the elements that appear in the list only once. The elements
must be printed in the order in which they occur in the original list.
Sample Input: 12 4 3 4 6 7 100 18 2 18 18
 Output: 12 3 6 7 100 2
"""
list1 = [12, 4, 3, 4, 6, 7, 100, 18, 2, 18, 18]
#type 1
dic = {}
for no in list1:
    if no not in dic:
        dic[no] = 1
    else:
        dic[no] += 1
for item, value in dic.items():
    if value == 1:
        print(item, end=' ')

print()

#type 2
from collections import Counter

di = Counter(list1)
for num in list1:
    if di[num] == 1:
        print(num, end=' ')