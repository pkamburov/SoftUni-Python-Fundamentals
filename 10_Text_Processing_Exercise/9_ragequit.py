text = input()
rage_message = ''
repetitions = ''
current_symbol = ''

for index in range(len(text)):
    if not text[index].isdigit():
        current_symbol += text[index].upper()
    else:
        for next_symbols in range(index, len(text)):
            if not text[next_symbols].isdigit():
                break
            repetitions += text[next_symbols]
        rage_message += current_symbol * int(repetitions)
        current_symbol = ''
        repetitions = ''
print(f"Unique symbols used: {len(set(rage_message))}")
print(rage_message)
