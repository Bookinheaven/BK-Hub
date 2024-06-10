"""
Follow the steps bellow: -Create a new dictionary called prices using {} format like

the example above.
● Put these values in your prices dictionary:
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
● Loop through each key in prices. For each key, print out the key along with
its price and stock information. Print the answer in the following format:
apple
price: 2
stock: 0
● Let's determine how much money you would make if you sold all of your
food.
o Create a variable called total and set it to zero.
o Loop through the prices dictionaries. For each key in prices, multiply
the number in prices by the number in stock. Print that value into the
console and then add it to total.
o Finally, outside your loop, print total.
"""

# 1
prices = {}
print(f"Created Dic: {prices}")
# 2 
prices.update(
    {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }
)
print(f"Prices: {prices}")

stock = {
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}

# 3 and 4
total = 0
for key, value in prices.items():
    for stock_name, stock_value in stock.items():
        if key == stock_name:
            total += value * stock_value
            print(f"{key}\nprices: {value}\nStock: {stock_value}\n")

print(f"Total: {total}")

print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")