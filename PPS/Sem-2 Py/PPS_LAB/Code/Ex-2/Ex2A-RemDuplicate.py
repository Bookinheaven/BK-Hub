"""
Write a Python program to remove duplicate elements in a list.
"""

list1 = []
list1 = input("Enter the Numbers: ").split(" ")
for x in list1:
    if x == ' ':
        list1.pop(list1)
list1 = set(list1)
print(f"List without duplicates: {list(list1)}")
print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")


