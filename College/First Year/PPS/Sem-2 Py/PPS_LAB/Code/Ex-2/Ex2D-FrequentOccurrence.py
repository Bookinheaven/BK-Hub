"""
Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
"""

# words = input("Enter the words: ")
# words = words.split(" ")
# unq_words = set(words)
# freq = 0
# check_word = input("Enter the word you want to check frequency: ")
# for x in range(len(words)):
#     if check_word == words[x]:
#         freq += 1
       
words = input("Enter the words: ")
words = words.split(" ")
unq_words = set(words)
word_freq = {} 
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print(f"Unique Words: {unq_words}")
print("Frequency:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")

print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")
