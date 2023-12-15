"""
Program that reverses a list without using built-in reverse functions.
"""

list1 = [1,2,3,4,5,6,7]
temp = []
for x in range(len(list1)):
    temp.append(list1[len(list1)-x-1])
list1 = temp 
del temp
print(list1)