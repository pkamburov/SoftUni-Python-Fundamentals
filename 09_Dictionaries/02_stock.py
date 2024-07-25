product_information = input().split()

stock_data = {}

for i in range(0, len(product_information), 2):
    product = product_information[i]
    quantity = int(product_information[i + 1])
    stock_data[product] = quantity


products_to_search = input().split()

for current_product in products_to_search:
    if current_product in stock_data:
        print(f"We have {stock_data[current_product]} of {current_product} left")
    else:
        print(f"Sorry, we don't have {current_product}")

print(stock_data)
