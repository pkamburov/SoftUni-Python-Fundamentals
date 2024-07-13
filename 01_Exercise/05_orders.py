n = int(input())
price = 0
total = 0

for i in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())
    price = (capsules_needed * price_per_capsule) * days
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 0 or days > 31:
        continue
    elif capsules_needed < 1 or capsules_needed > 2000:
        continue
    print(f'The price for the coffee is: ${price:.2f}')
    total += price
print(f'Total: ${total:.2f}')
