list_of_gifts = input().split()
command = ''

while command != "No Money":
    command = input()
    if command == "No Money":
        break
    split = command.split()

    if split[0] == "OutOfStock":
        gift_to_remove = split[1]
        for i in range(len(list_of_gifts)):
            if list_of_gifts[i] == gift_to_remove:
                list_of_gifts[i] = "None"
    elif split[0] == "Required":
        index = int(split[2])
        if 0 <= index < len(list_of_gifts):
            list_of_gifts[index] = split[1]
    elif split[0] == "JustInCase":
        list_of_gifts[-1] = split[1]

filtered_gifts = [split for split in list_of_gifts if split != "None"]
print(" ".join(filtered_gifts))

