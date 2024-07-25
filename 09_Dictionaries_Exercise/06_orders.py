products = {}

while True:
    input_info = input()
    if input_info == 'buy':
        break

    name, price, quantity = input_info.split()
    price = float(price)
    quantity = int(quantity)

    if name in products:
        products[name]['price'] = price
        products[name]['quantity'] += quantity
    else:
        products[name] = {'price': price, 'quantity': quantity}

for product, info in products.items():
    total_price = info['price'] * info['quantity']
    print(f"{product} -> {total_price:.2f}")
