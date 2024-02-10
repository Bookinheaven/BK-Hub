"""
Write python functions to print the no. of uppercase, lowercase, and whitespaces.
Sample Input :
Enter any string: Hello, Welcome to Karunya
Sample output:
Uppercase: 3
Lowercase: 18
Whitespaces: 3
"""

def check_space(sent):
    count = 0
    for char in sent:
        if char.isspace():
            count += 1
    return count
def check_lower(sent):
    count = 0
    for char in sent:
        if char.islower():
            count += 1
    return count
def check_upper(sent):
    count = 0
    for char in sent:
        if char.isupper():
            count += 1
    return count
            
check_str = input("Enter the str: ")
print(f"Uppercase: {check_upper(check_str)}")
print(f"Lowercase: {check_lower(check_str)}")
print(f"Whitespaces: {check_space(check_str)}")
print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")