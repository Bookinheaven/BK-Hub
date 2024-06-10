"""
Write a Python program to extract the word starting in vowels from a text file and print the same.
"""
with open("srcF.txt", "r") as srcfile:
    reada = (srcfile.read()).split(" ")
    vowels = ["a", "e", "i", "o", "u"]
    print("Vowels Words: ", end = " ")
    for word in reada:
        for vow in vowels:
            if word.startswith(vow):
                print(word, end = " ")
print("\n╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")