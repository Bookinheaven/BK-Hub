# Write a python program to check whether a number is a palindrome or not using a function
def check_palindrome(item):
    return item[::-1] 
check_num = (input("Enter the number: ")).strip()
result = check_palindrome(check_num)
if result == check_num:
    print(f"Its {check_num} is a Palindrome!")
else:
    print(f"Its {check_num} is not a Palindrome!")
print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")