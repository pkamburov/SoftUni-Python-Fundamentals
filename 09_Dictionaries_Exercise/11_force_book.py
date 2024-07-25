force_side_dict = {}
command = input()

while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        user_is_part = False
        for value in force_side_dict.values():
            if force_user in value:
                user_is_part = True
                break
        if not user_is_part:
            if force_side not in force_side_dict.keys():
                force_side_dict[force_side] = []
            force_side_dict[force_side].append(force_user)
    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        for value in force_side_dict.values():
            if force_user in value:
                value.remove(force_user)
                break
        if force_side not in force_side_dict.keys():
            force_side_dict[force_side] = []
        force_side_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()

for force_side, force_users in force_side_dict.items():
    if len(force_users) > 0:
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for force_user in force_users:
            print(f"! {force_user}")
