command = ''
coffee_counter = 0

while command != "END":
    if command.lower() == "coding" \
            or command == "dog" \
            or command == "cat" \
            or command == "movie":
        if command.islower():
            coffee_counter += 1
        else:
            coffee_counter += 2
    elif command.upper() == "CODING" \
            or command == "DOG" \
            or command == "CAT" \
            or command == "MOVIE":
        if command.islower():
            coffee_counter += 1
        else:
            coffee_counter += 2
    command = input()

if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(f"{coffee_counter}")
