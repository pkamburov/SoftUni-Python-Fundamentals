def is_valid(i, ship):
    return 0 <= i < len(ship)


def fire(ship, i, dmg):
    if is_valid(i, ship):
        warship[i] -= dmg
        if ship[i] <= 0:
            print(f"You won! The enemy ship has sunken.")
            exit()


def defend(ship, start, end, dmg):
    if is_valid(start, ship) and is_valid(end, ship):
        for i in range(start, end + 1):
            ship[i] -= dmg
            if ship[i] <= 0:
                print(f"You lost! The pirate ship has sunken.")
                exit()


def repair(ship, i, amount, maximum):
    if is_valid(i, ship):
        ship[i] = min(ship[i] + amount, maximum)


def status(ship, maximum):
    count = sum(1 for section in ship if section < 0.2 * maximum)
    print(f'{count} sections need repair.')


pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health = int(input())
counter = 0

while True:
    command = input().split()
    current_command = command[0]
    if current_command == "Retire":
        break

    elif current_command == "Fire":
        index, damage = int(command[1]), int(command[2])
        fire(warship, index, damage)

    elif current_command == "Defend":
        start_index, end_index, damage = int(command[1]), int(command[2]), int(command[3])
        defend(pirate_ship, start_index, end_index, damage)

    elif current_command == "Repair":
        index, health = int(command[1]), int(command[2])
        repair(pirate_ship, index, health, max_health)

    elif current_command == "Status":
        status(pirate_ship, max_health)


print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship)}")

# 12>13>11>20>66
# 12>22>33>44>55>32>18
# 70
# Fire 2 11
# Fire 8 100
# Defend 3 6 11
# Defend 0 3 5
# Repair 1 33
# Status
# Retire

# 2>3>4>5>2
# 6>7>8>9>10>11
# 20
# Status
# Fire 2 3
# Defend 0 4 11
# Repair 3 1
# Retire