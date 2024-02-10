# Write a python program to check Armstrong number using functions
def armstrong(item):
    result = 0
    leng = len(item)
    for i in item:
        result += int(i) ** leng
    return result
check_num = (input("Enter the number: ")).strip()
result = armstrong(check_num)
if result == int(check_num):
    print(f"Its {check_num} is an Armstrong Number!")
else:
    print(f"Its {check_num} is not an Armstrong Number!")
print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")