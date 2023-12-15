"""
program that finds the second largest number in a list.
"""

list1 = [12,1,11,42,121,11,86,999,7]
largest = 0
for x in range(len(list1)):
    if (list1[x] >= largest):
        largest = list1[x]

print(f"Largest: {largest}")