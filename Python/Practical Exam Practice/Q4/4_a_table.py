"""
Write a program that computes an investment report.
The inputs to this program are the following:
 An initial amount to be invested (a floating-point number)
 A period of years (an integer)
 An interest rate (a percentage expressed as an integer)
Sample Input
Enter the investment amount: 10000.00
Enter the number of years: 5
Enter the rate as a %: 5
"""

invest = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = int(input("Enter the rate as a %: "))

data = {
    "Year": [num for num in range(1, years+1)],
    "Starting balance": [invest],
    "Interest": [],
    "Ending balance": []
}
for num in range(1, years+1):
    intrest = data['Starting balance'][num-1] * rate/100
    ending_balance = data['Starting balance'][num-1]+intrest
    starting_balance = ending_balance
    data['Interest'].append(intrest)
    data['Ending balance'].append(intrest)
    data['Starting balance'].append(starting_balance)

print("{:<6s}{:<20s}{:<12s}{:<15s}".format('Year', 'Starting balance', 'Interest', 'Ending balance'))

for i in range(len(data['Year'])):
    print("{:<6d}{:<20.2f}{:<12.2f}{:<15.2f}".format(data['Year'][i], data['Starting balance'][i], data['Interest'][i], data['Ending balance'][i]))
