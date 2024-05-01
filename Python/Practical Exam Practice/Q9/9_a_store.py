"""
Read 10 integer numbers as input and store it in a list variable and find all numbers that are
multiples of both 2 and 8 and display the same in a List format

"""
num = input('Enter 10 numbers: ').strip().split()[0:11]
mul = [x for x in num if int(x) % 2 == 0 and int(x) % 8 == 0]
print(mul)

