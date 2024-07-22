def is_valid_index(ship, i):
    return 0 <= i < len(ship)


pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
maximum_health_capacity = int(input())
command = ""
lost = False
won = False

while True:
    command = input().split()
    if command[0] == "Retire":
        break

    if command[0] == "Fire":
        index, damage = int(command[1]), int(command[2])
        if is_valid_index(warship, index):
            warship[index] -= damage
            if int(warship[index]) <= 0:
                print(f"You won! The enemy ship is sunken.")
                won = True
                break

    elif command[0] == "Defend":
        start_index, end_index, damage = int(command[1]), int(command[2]), int(command[3])
        if is_valid_index(pirate_ship, start_index) and is_valid_index(pirate_ship, end_index):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    lost = True
                    break

    elif command[0] == "Repair":
        index, health = int(command[1]), int(command[2])
        if is_valid_index(pirate_ship, index):
            if pirate_ship[index] + health >= maximum_health_capacity:
                pirate_ship[index] = maximum_health_capacity
            else:
                pirate_ship[index] += health

    elif command[0] == "Status":
        count = 0
        for section in pirate_ship:
            if section < maximum_health_capacity * 0.2:
                count += 1
        print(f"{count} sections need repair.")

if not won and not lost:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
