"""
Create a program that reads a text file(eg. “abc.txt”) and do the following
 Read all the four-letter words and write in another file called “four.txt”
 Read all the vowels and write in another file called “vowels.txt”
 Read all the consonants and write in another file called “consonants.txt”
"""
import os
filepath = os.path.join(os.path.dirname(__file__), 'textfile.txt')
four_letter_words = []
consonants = []
vowels = []
with open(file=filepath, mode='r') as mainfile:
    data = mainfile.read().strip().split()
    # four letter words
    for word in data:
        if len(word) == 4:
            four_letter_words.append(word)
        if word[0].lower() in ['a','e','i','o','u']:
            vowels.append(word)
        else:
            consonants.append(word)
    with open(file=os.path.join(os.path.dirname(__file__), 'four.txt'), mode='w') as four :
        four.write(" ".join(four_letter_words))
    with open(file=os.path.join(os.path.dirname(__file__), 'vowels.txt'), mode='w') as vowel_file :
        vowel_file.write(" ".join(vowels))
    with open(file=os.path.join(os.path.dirname(__file__), 'consonants.txt'), mode='w') as conson :
        conson.write(" ".join(consonants))