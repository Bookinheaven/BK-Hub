"""
Task: Temperature Conversion

Create a Python program that converts temperatures between Celsius and
Fahrenheit. Prompt the user to enter a temperature value and the unit of
measurement, and then display the converted temperature.
"""

def celsiusToFahrenheit(celsius: float):
    return (celsius * 9/5) + 32

def fahrenheitToCelsius(fahrenheit: float):
    return (fahrenheit - 32) * 5/9

try:
    # Prompt user for temperature value
    tempValue: float = float(input("Enter the temperature value: "))

    # Prompt user for unit of measurement
    unit: str = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ").upper()

    if unit == 'C':
        converted_temp: float = celsiusToFahrenheit(tempValue)
        print(f"{tempValue}°C is equal to {converted_temp:.2f}°F")
    elif unit == 'F':
        converted_temp: float = fahrenheitToCelsius(tempValue)
        print(f"{tempValue}°F is equal to {converted_temp:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

except Exception as e:
    print(f"Exception: {e}")