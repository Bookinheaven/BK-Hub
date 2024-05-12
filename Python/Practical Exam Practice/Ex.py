# Write a Python program to find the factorial of a number using while loop

num = 5 
final = 1
while num > 1: 
    final *= num
    num -= 1
print(final)

# Write a Python program to check whether a number is Prime or not

num = 11
def prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
if prime(num):
    print('Its Prime Number')
else:
    print('Not A prime number')

# Write a Python program that iterates the integers from 1 to 15. For multiples of two print
# "Karunya" instead of the number and for the multiples of three print "University". For
# numbers which are multiples of both two and three print "KarunyaUniversity".

for x in range(1, 16):
    if x % 2 == 0 and x % 3 == 0:
        print('KarunyaUniversity')
    elif x % 2 == 0:
        print("Karunya")
    elif x % 3 == 0:
        print("University")

# Write a python program to check whether the number is palindrome or not.

num = 121
fake = num
final = 0
while fake > 0:
    final = final * 10 + fake % 10
    fake //= 10
if num == final:
    print('Its palindrome')
else:
    print('Its not palindrome')

# Write a python program to check whether the number is Armstrong number or not.

num = 153
final = 0
for x in str(num):
    final += int(x)**3
print(final)

# Write a Python program to find the second smallest and Second largest number in a list.

lis1 = [1, 55,2,34,12,56]
smallest = second_smallest = float('inf')
largest = second_largest = float('-inf')

for num in lis1:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print(second_smallest, second_largest)

# Write a Python program to get the frequency of the elements in a list.

list1 = [5,1,2,5,12,31,2]
feq = {}
for x in list1:
    if x in feq:
        feq[x] += 1
    else:
        feq[x] = 1
for element, count in feq.items():
    print(element, ':',count)
