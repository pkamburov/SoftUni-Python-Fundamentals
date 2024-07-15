# Define the maximum prices for each item type
max_prices = {
    "Clothes": 50.00,
    "Shoes": 35.00,
    "Accessories": 20.50,
}

# Read the input
items_input = input()
budget = float(input())

# Parse the items and their prices from the input
items = {}
item_data = items_input.split('|')
for item_data_str in item_data:
    item_price = item_data_str.split('->')
    item = item_price[0]
    price = float(item_price[1])
    items[item] = price

# Initialize variables to keep track of bought items and profit
bought_items = {}
profit = 0.0

# Buy items within budget and update profit
for item, price in items.items():
    if price <= max_prices.get(item, 0) and budget >= price:
        bought_items[item] = price
        profit += 0.4 * price
        budget -= price

# Increase the price of bought items by 40%
for item in bought_items:
    bought_items[item] += 0.4 * bought_items[item]

# Check if the budget is enough for the train ticket
if budget >= 150:
    bought_prices_str = " ".join([f'{price:.2f}' for price in bought_items.values()])
    print(bought_prices_str)
    print(f"Profit: {profit:.2f}")
    print("Hello, France!")
else:
    bought_prices_str = " ".join([f'{price:.2f}' for price in bought_items.values()])
    print(bought_prices_str)
    print(f"Profit: {profit:.2f}")
    print("Not enough money.")
