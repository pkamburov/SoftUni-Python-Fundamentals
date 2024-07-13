command = ''

while command != 'End':
    command = input()
    if command == 'SoftUni':
        continue
    elif command == 'End':
        break
    new_string = ''
    for character in command:
        new_string += character * 2
    print(new_string)
