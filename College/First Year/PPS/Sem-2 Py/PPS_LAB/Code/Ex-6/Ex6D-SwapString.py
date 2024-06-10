"""
Write a Python program to find the first appearance of the substring 'not' and 'bad'
from a given string, if 'not' follows the 'bad', replace the whole 'not'...'bad'
substring with 'good'. Return the resulting string.
Sample Input :
The song is not that bad!
The song is poor!
Sample Output:
The song is good!
The song is poor!
"""

string1 = (input("Enter the String: ").strip()).split(" ")
string2 = (input("Enter the String: ").strip()).split(" ")
for string in [string1, string2]:
    for x in range(0, len(string)):
        if string[x] == 'not': 
            if string[x+2] == 'bad!':
                string[x] = 'good!'
                string[x+2] = ''
                string[x+1] = ""
    print(*string)
