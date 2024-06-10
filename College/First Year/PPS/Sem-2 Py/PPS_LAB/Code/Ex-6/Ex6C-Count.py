"""
Write a Python program to find characters count of a string which are passed as list.
Input: St="hello welcome" lst=[“l", "w", "m", "e"]
Output:
l 3
w 1
m 1
e 3
"""

string = input("Enter the String: ")
list1 = (input("Enter the letters you want to find: ").strip()).split(" ")
list2 = [string.count(x) for x in list1]
for letter, no in zip(list1,list2):
    print(f"{letter} {no}")
