"""
Develop a program that searches for an element in a list and returns its index.
"""

list1 = [1,2,3,4,5,6,7,8]
input_value = int(input("Enter the value: "))
for index, value in enumerate(list1):
    if(value == input_value):
        print(f"Value: {value}\nIndex: {index}")