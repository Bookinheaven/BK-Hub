"""
Given an integer, N, perform the following conditional actions:
 If N is odd, print Weird
 If N is even and in between 5 to 11, print Not Weird
 If N is even and in between 13 to 35 , print Weird
 If N is even and greater than 36, print Not Weird
"""

num = int(input("Enter the number: "))
if num % 2 == 1:
    print('Weird')
elif num % 2 == 0 :
    if 5 <= num <= 11:
        print('Not Weird')
    elif 13 <= num <= 35:
        print('Weird')
    elif num >= 36:
        print('Not Weird')