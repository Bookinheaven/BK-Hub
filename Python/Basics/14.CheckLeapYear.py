"""
Write a python program to check leap year or not
"""

year = input("Enter the year: ")

if year.isdigit():
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f'Given ({year}) is a Leap Year')
    else:
        print(f'Given ({year}) is Not a Leap Year')
else:
    print("Wrong enter the integer year!")
