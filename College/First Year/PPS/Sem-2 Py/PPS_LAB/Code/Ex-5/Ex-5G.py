"""
7. Write a Python program to create a file where all letters of the English alphabet are listed by
the specified number of letters on each line based on the input ‘n’
Sample Input: 5
Sample output:
ABCDE

FGHIJ
KLMNO
PQRST
UVWXY
Z.
"""

num = int(input("Enter the no: "))
aplha = "abcdefghijklmnopqrstuvwxyz".upper()
with open("fileG.txt", "w") as file:
    for no, letter in enumerate(aplha, start=1):
        file.write(letter)
        if no % num == 0:
            file.write("\n")
    print("Done:")