# 8. Write a Python program to read the first n lines of a file.
num = int(input("Enter the line no: "))
with open("srcH.txt", "r") as file:
    data = (file.read()).split("\n")
    print(f"Line ({num}): {data[num-1]}")
print("\n╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")