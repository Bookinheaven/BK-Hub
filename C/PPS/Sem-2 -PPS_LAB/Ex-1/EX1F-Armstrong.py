print("Ex1 F)Write a python program to check whether the number is Armstrong number or not.\nResult")

num = int(input("Enter the number: "))
arm, i= 0, num
while i > 0:
    arm += (i % 10) ** 3
    i //= 10

if(arm== num):
    print("Its a Armstrong Number!")
else:
    print("Its not a Armstrong Number!")

print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")