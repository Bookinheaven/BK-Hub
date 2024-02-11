"""
Write a python program to find the longest word in a file
"""
def find_longest_word(file_path):
    longest_word = ""
    with open(file_path, 'r') as file:
        words = (file.read()).split()
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word
                
    return longest_word

longest_word = find_longest_word("srcC.txt")
print("The longest word in the file is:", longest_word)
