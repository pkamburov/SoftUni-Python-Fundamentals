sequence_of_strings = input()
strings = sequence_of_strings.split()
total_sum = 0

for string in strings:
    number = ''
    for character in string:
        if character.isdigit():
            number += character
    number = int(number)
    if string[0].isupper():
        position = ord(string[0]) - 64
        result = number / position
    else:
        position = ord(string[0]) - 96
        result = number * position

    if string[-1].isupper():
        position = ord(string[-1]) - 64
        result -= position
    else:
        position = ord(string[-1]) - 96
        result += position
    total_sum += result


print(f"{total_sum:.2f}")
