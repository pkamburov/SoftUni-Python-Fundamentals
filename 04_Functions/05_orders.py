def calculate_price(item, quantity):
    if item == "coffee":
        return f"{1.50 * quantity:.2f}"
    elif item == "coke":
        return f"{1.40 * quantity:.2f}"
    elif item == "water":
        return f"{1.00 * quantity:.2f}"
    elif item == "snacks":
        return f"{2.00 * quantity:.2f}"


item = input()
quantity = int(input())

print(calculate_price(item, quantity))
