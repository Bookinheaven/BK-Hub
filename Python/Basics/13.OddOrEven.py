"""
Write a python program to check odd or even number
"""

num = input("Enter the number: ")
if num.isdigit():
    if int(num) % 2 == 0:
        print(f'Given ({num}) Even Number')
    else:
        print(f'Given ({num}) Odd Number')
else:
    print("Wrong enter the integer number!")