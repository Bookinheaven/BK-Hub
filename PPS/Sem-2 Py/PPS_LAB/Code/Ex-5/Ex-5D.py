"""
Write a Python Program to read a file’s entire content and store it back in another file in a reverse manner.
Ex: hi how are you? hope you are fine?
output: fine? are you hope you? are how hi
""" 
with open("src.txt", "r") as srcfile:
    reada = srcfile.read()
    with open ("des.txt", "w") as desfile:
        desfile.write(" ".join((reada.split(" "))[::-1]))
        print("Successfully read a files entire content and stored it back in des.txt file in a reverse manner")
print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")