"""
Python program that converts temperature from Celsius to Fahrenheit using user input and type conversion
"""
def temp_change(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter the Value of Celsius: "))
print(f"Fahrenheit: {temp_change(celsius)}")

