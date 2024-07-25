legendary_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
obtained = False

while not obtained:
    current_items = input().split()
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()

        if key not in legendary_materials.keys():
            legendary_materials[key] = 0
        legendary_materials[key] += value

        if legendary_materials["shards"] >= 250:
            obtained = True
            legendary_materials['shards'] -= 250
            print('Shadowmourne obtained!')
        elif legendary_materials['fragments'] >= 250:
            obtained = True
            legendary_materials['fragments'] -= 250
            print('Valanyr obtained!')
        elif legendary_materials['motes'] >= 250:
            obtained = True
            legendary_materials['motes'] -= 250
            print('Dragonwrath obtained!')
        if obtained:
            break

for material, quantity in legendary_materials.items():
    print(f"{material}: {quantity}")
