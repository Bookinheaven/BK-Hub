"""
Write a Python function to use the arbitrary function by getting a sequence of numbers as input
and only print the divisors of the last input from the passing numbers.
Sample input:
function with a sequence of numbers
fun1(6, 7, 8)
fun1(1, 2, 5, 7, 9)
fun1(1, 3, 5, 7, 9, 12)
Sample Output:
8 : 1 2 4 8
9 : 1 3 9
12 : 1 2 3 4 6 12
"""

def fun1(*args):
    last_item = args[-1]
    result = [x for x in range(1, last_item + 1) if last_item % x == 0]
    print(f"{last_item} :"," ".join(map(str, result)))
fun1(6, 7, 8)
fun1(1, 2, 5, 7, 9)
fun1(1, 3, 5, 7, 9, 12)
print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")
