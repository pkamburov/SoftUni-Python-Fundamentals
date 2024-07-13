budget = float(input())
flour_price = float(input())

eggs_price_per_pack = flour_price * 0.75
milk_price_per_litre = flour_price + flour_price * 0.25
milk_price_per_bread = milk_price_per_litre / 4
price_per_bread = eggs_price_per_pack + milk_price_per_bread + flour_price
breads_made = 0
colored_eggs = 0

while budget > 0:
    if budget - price_per_bread < 0:
        break
    budget -= price_per_bread
    breads_made += 1
    colored_eggs += 3
    if breads_made % 3 == 0:
        colored_eggs -= breads_made - 2

print(f'You made {breads_made} loaves of Easter bread! '
      f'Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
