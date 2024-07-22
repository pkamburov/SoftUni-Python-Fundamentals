starting_list = input().split()
number_of_commands = int(input())

for command in range(number_of_commands):
    current_command = input().split()
    if current_command[0] == "Include":
        starting_list.append(current_command[1])
    elif current_command[0] == "Remove":
        if current_command[1] == "first" and len(starting_list) > int(current_command[2]):
            number_of_removed = int(current_command[2])
            for i in range(number_of_removed):
                starting_list.remove(starting_list[0])
        elif current_command[1] == "last" and len(starting_list) > int(current_command[2]):
            number_of_removed = int(current_command[2])
            for i in range(number_of_removed):
                starting_list.pop()
    elif current_command[0] == "Prefer":
        if int(current_command[1]) <= len(starting_list) and int(current_command[2]) <= len(starting_list):
            index1 = int(current_command[1])
            index2 = int(current_command[2])
            starting_list[index1], starting_list[index2] = starting_list[index2], starting_list[index1]
    elif current_command[0] == "Reverse":
        starting_list.reverse()


format_list = ' '.join(map(str, starting_list))
print(f"Coffees:\n"
      f"{format_list}")
