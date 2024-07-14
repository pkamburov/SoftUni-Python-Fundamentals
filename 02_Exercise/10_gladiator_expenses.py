lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmets_count = 0
sword_count = 0
shield_count = 0
armor_count = 0


for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        helmets_count += 1
    if i % 3 == 0:
        sword_count += 1
        if i % 2 == 0:
            shield_count += 1
            if shield_count % 2 == 0:
                armor_count += 1

total_cost = helmets_count * helmet_price + \
             sword_count * sword_price + \
             shield_count * shield_price + \
             armor_count * armor_price

print(f'Gladiator expenses: {total_cost:.2f} aureus')
