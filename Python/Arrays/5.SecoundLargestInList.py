"""
program that finds the second largest number in a list.
"""

list1 = [12, 1, 11, 42, 121, 11, 86, 999, 7]
largest = float('-inf')
second_largest = float('-inf')

for number in list1:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number

print(f"Second Largest: {second_largest}")
