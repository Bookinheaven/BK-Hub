"""
Write a Python function that accepts a file and performs the following operation,
• calculate the number of upper-case letters and lower-case letters
from the entire content of the file.
• Search a word in a particular line
• Search a word in the range of lines
• Replace a word in the file
"""
def count_upper_lower(file_path):
    upper_count = 0
    lower_count = 0

    with open(file_path, 'r') as file:
        content = file.read()
        for char in content:
            if char.isupper():
                upper_count += 1
            elif char.islower():
                lower_count += 1

    return upper_count, lower_count

def search_word_in_line(file_path, line_number, word):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return word in lines[line_number - 1]

def search_word_in_range(file_path, start_line, end_line, word):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[start_line - 1:end_line]:
            if word in line:
                return True
        return False

def replace_word_in_file(file_path, old_word, new_word):
    with open(file_path, 'r+') as file:
        content = file.read()
        content = content.replace(old_word, new_word)
        file.seek(0)
        file.write(content)
        file.truncate()

file_path = 'srcA.txt'

upper_count, lower_count = count_upper_lower(file_path)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)

line_number = 3
word_to_search = 'bot'
print("Word '{}' found in line {}: {}".format(word_to_search, line_number, search_word_in_line(file_path, line_number, word_to_search)))

start_line = 1
end_line = 5
print("Word '{}' found in lines {} to {}: {}".format(word_to_search, start_line, end_line, search_word_in_range(file_path, start_line, end_line, word_to_search)))

old_word = 'bot'
new_word = 'rat'
replace_word_in_file(file_path, old_word, new_word)
print("Word '{}' replaced with '{}' in the file.".format(old_word, new_word))
