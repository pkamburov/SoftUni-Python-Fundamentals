number_of_commands = int(input())
registered = {}

for i in range(number_of_commands):
    command_data = input().split()
    if command_data[0] == 'register':
        command, name, number_plate = command_data
        if name not in registered.keys():
            registered[name] = number_plate
            print(f"{name} registered {number_plate} successfully")
        elif name in registered.keys():
            print(f"ERROR: already registered with plate number {number_plate}")

    elif command_data[0] == 'unregister':
        command, name = command_data
        if name not in registered.keys():
            print(f"ERROR: user {name} not found")
        elif name in registered.keys():
            print(f"{name} unregistered successfully")
            del registered[name]

for name, number_plate in registered.items():
    print(f"{name} => {number_plate}")
