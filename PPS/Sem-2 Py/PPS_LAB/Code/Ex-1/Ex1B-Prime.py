print("Ex-1 B)Program to check whether a number is Prime or not\nResult:")
num = int(input("Enter the number: "))

if num < 2:
    print(f"Given number ('{num}') is not Prime")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"Given number ('{num}') is Prime")
    else:
        print(f"Given number ('{num}') is not Prime")

print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")