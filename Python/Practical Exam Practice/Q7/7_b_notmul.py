"""
Given a list A of numbers (integers), you have to print those numbers which are not multiples of
5.
Sample Input: 10 4 11 15 45 8 50
Output: 4 11 8
"""
num = input("Enter the numbers: ").strip().split()
for no in num:
    no = int(no)
    if no % 5 == 0:
        print(no, end=" ")    