"""
Write a Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form (alphanumerically).
Sample Input: red, black, pink, green
Sample Output: black, green, pink, red
"""

colors = input("Enter the colors: ").split(",")
order1 = [x.strip() for x in colors]
order1 = set(order1)
order1 = list(order1)
order1.sort()
print("Output: ", end ="")
print(*order1, sep=", ")
