"""
Python program to calculate the area of a rectangle using variables for length and width.
"""

def area(leng, wid):
    return leng*wid

lenght = int(input("Enter the Length of the Rectangle: "))
width = int(input("Enter the Width of the Rectangle: "))
print(f"Area of Rectangle: {area(leng=lenght,wid=width)}")
