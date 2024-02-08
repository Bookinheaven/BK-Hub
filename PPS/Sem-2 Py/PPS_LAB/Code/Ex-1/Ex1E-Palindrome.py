print("Ex-1 E)Write a program to check whether the number is palindrome or not.\nResult:")

num = int(input("Enter the number: "))
pal, i= 0,num

while i > 0:
    pal = pal* 10 + (i % 10)
    i //= 10 

if(pal== num):
    print("Its a Palindrome Number!")
else:
    print("Its not a Palindrome Number!")

print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")