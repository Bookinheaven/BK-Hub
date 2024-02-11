# Write a Python program to count the frequency of words in a file

with open("srcI.txt", "r") as src_file:
    data = (((src_file.read()).replace("\n", "")).strip()).split(" ")
    print(f"Frequency of words: {len(data)}")
print("\n╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")