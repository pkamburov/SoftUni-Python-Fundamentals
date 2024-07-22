chat = []

while True:
    command = input().split()
    if command[0] == "end":
        break

    if command[0] == "Chat":
        chat.append(command[1])

    elif command[0] == "Delete":
        if command[1] in chat:
            chat.remove(command[1])

    elif command[0] == "Edit":
        if command[1] in chat:
            index = chat.index(command[1])
            chat[index] = command[2]
    elif command[0] == "Pin":
        if command[1] in chat:
            length = len(chat)
            chat.remove(str(command[1]))
            chat.insert(length-1, str(command[1]))

    elif command[0] == "Spam":
        for i in range(1, len(command)):
            chat.append(command[i])

format_chat = ' '.join(map(str, chat))

for word in chat:
    print(word)
