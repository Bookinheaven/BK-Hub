"""
Develop a program to read a text file and do the following
 Display the number of words
 Display the number of alphabets
 Display the number of digits
 Display the number of spaces
"""
import os
textfile_path = os.path.join(os.path.dirname(__file__), 'readfile.txt')

num_of_words = num_of_alphabets = num_of_digits = num_of_spaces = 0

with open(file=textfile_path, mode='r') as file:
    data = file.readlines()
    for line in data:
        for char in line:
            if char.isspace():
                num_of_spaces += 1
        line = line.split(" ")
        for word in line:
            if word.isalpha():
                num_of_words += 1
                for apha in word:
                    if apha.isalpha():
                        num_of_alphabets += 1
            if word.isdigit():
                num_of_digits += 1

        
print(f"No of words: {num_of_words}\nNo of alphabets: {num_of_alphabets}\nNo of digits: {num_of_digits}\nNo of spaces: {num_of_spaces}")