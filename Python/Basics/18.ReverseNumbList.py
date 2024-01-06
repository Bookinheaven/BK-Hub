
num = input("Enter the list: ")
list1 = []
for n in num:
    if n != ' ':
        list1.append(n)

print(list1)
print(list1[::-1])