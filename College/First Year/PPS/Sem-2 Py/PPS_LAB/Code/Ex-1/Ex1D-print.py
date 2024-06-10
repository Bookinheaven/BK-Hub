print(r"""Ex-1 D)Program that iterates the integers from 1 to 15. For multiples of two print
"Karunya" instead of the number and for the multiples of three print 'University'. 
For numbers which are multiples of both two and three print 'KarunyaUniversity'""","\nResult:")


num = int(input("Enter the number: "))

str1 = "Karunya"
str2 = "University"

for x in range(1,num+1):
    if(x % 2 == 0 and x % 3 == 0):
        print(str1+str2)
    elif(x % 2 == 0):
        print(str1)
    elif(x % 3 == 0):
        print(str2)
print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")


