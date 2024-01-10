"""
Write a Python program to remove duplicate elements in a list.
"""

list1 = input("Enter the Numbers: ").split()
list1 = list(set(list1)- {''})
print(f"List without duplicates: {list1}")
print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")