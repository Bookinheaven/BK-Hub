"""
Create a program to store the given words in a list and display the word starting with given
vowels (get as input).
Sample Input:
Enter the words: email welcome easy elephant
Enter the vowel letter: e
Output:
The words are:
email
easy
elephant"""


words = input('Enter the words: ').strip().split()
let = input('Enter the vowel letter: ').strip()
if let.lower() not in ['a','e','i','o','u']:
    print("Its not a vowel")
else:
    print('The words are:')
    for x in words:
        if x.startswith(let.lower()):
            print(x)