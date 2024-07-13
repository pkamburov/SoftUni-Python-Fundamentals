command = ''
count = 0

while command != "Welcome!":
    command = input()
    count = 0
    if command == "Voldemort":
        print("You must not speak of that name!")
        break
    elif command == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    for i in range(0, len(command)):
        count += 1
    if count < 5:
        print(f"{command} goes to Gryffindor.")
    elif count == 5:
        print(f"{command} goes to Slytherin.")
    elif count == 6:
        print(f"{command} goes to Ravenclaw.")
    else:
        print(f"{command} goes to Hufflepuff.")
