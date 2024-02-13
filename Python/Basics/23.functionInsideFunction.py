"""
Write a Python program to access a function inside a function.
"""

def outer():
    print("Im outside")
    def inner():
        return print("Im Inside")
    inner()

outer()