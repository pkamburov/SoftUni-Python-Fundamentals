items_list = input().split("|")
budget = float(input())
remaining_budget = budget

items_bought = []
profit = 0

for each_item in items_list:
    item_type, item_price = each_item.split("->")
    item_price = float(item_price)

    if item_type == "Clothes":
        if item_price <= 50.00 and remaining_budget >= item_price:
            remaining_budget -= item_price
            items_bought.append(item_price)
            profit += item_price * 0.4
    elif item_type == "Shoes":
        if item_price <= 35.00 and remaining_budget >= item_price:
            remaining_budget -= item_price
            items_bought.append(item_price)
            profit += item_price * 0.4
    elif item_type == "Accessories":
        if item_price <= 20.50 and remaining_budget >= item_price:
            remaining_budget -= item_price
            items_bought.append(item_price)
            profit += item_price * 0.4

items_bought = [round(item * 1.4, 2) for item in items_bought]
bought_items = (' '.join(map(str, items_bought)))

print(bought_items)
print(f"Profit: {profit:.2f}")

total = round(budget + profit, 2)

if total >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
