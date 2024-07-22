health = 100
bitcoins = 0
room_count = 0
is_killed = False

rooms = input().split('|')

for room in rooms:
    room_count += 1
    command, number = room.split()
    if command == "potion":
        temp_health = health
        health += int(number)
        if health > 100:
            health = 100
        healed_amount = health - temp_health
        print(f"You healed for {healed_amount} hp.\n"
              f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins_found = int(number)
        bitcoins += bitcoins_found
        print(f"You found {bitcoins_found} bitcoins.")
    else:
        health -= int(number)
        if health > 0:
            print(f"You slayed {command}.")
        else:
            is_killed = True
            break

if is_killed:
    print(f"You died! Killed by {command}.\n"
          f"Best room: {room_count}")
else:
    print(f"You've made it!\n"
          f"Bitcoins: {bitcoins}\n"
          f"Health: {health}")
