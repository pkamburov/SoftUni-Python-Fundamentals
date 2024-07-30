while True:
    word = input()

    if word.lower() == 'end':
        break

    print(f"{word} = {word[::-1]}")
