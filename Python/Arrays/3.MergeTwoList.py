"""
Create a program that merges two lists and removes duplicates.
"""

list1 = [1,2,3,4,5,6,7]
list2 = [1,2,8,64,33,21]
list3 = set(list1 + list2) #set removes duplicates because it wont accept it
print(list(list3))