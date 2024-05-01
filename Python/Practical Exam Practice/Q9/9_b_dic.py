"""
Create the following two dictionaries:
1. The Products dictionary contains the product names and prices
"TV": 400, "DVD": 10, "Memory Card": 20, "Pen Drive": 100
2. The Stock dictionary contains the quantity of each products
"TV": 2, "DVD": 5, "Memory Card": 6, "Pen Drive": 3
Let's determine how much money you would make if you sold all of your products.
 Create a variable called total and set it to zero.
 Loop through the price’s dictionaries. For each key in prices, multiply the number in
prices by the number in stock. Print that value into the console and then add it to total.
 Finally, outside your loop, print total
"""

products = {
    "TV": 400,
    "DVD": 10,
    "Memory Card": 20,
    "Pen Drive": 100
}

stock = {
    "TV": 2,
    "DVD": 5,
    "Memory Card": 6,
    "Pen Drive": 3
}

total = 0

for product, price in products.items():
    if product in stock:
        total += price * stock[product]
        print(f"Revenue from {product}: {price * stock[product]}")
    else:
        print(f"Product {product} not found in stock.")

print("Total revenue:", total)
