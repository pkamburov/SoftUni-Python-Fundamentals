def all_characters(first: str, second: str):
    characters = []
    for current_character in range(ord(first) + 1, ord(second)):
        characters.append(chr(current_character))
    return characters


first_char = input()
second_char = input()

result = ' '.join(all_characters(first_char, second_char))
print(result, ' ')
