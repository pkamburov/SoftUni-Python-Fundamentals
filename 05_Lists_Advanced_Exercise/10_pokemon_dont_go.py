def catch_pokemon(sequence, index):
    if len(sequence) == 0:
        return 0

    if index < 0:
        removed_element = sequence.pop(0)
        sequence.insert(0, sequence[-1])
    elif index >= len(sequence):
        removed_element = sequence.pop()
        sequence.append(sequence[0])
    else:
        removed_element = sequence.pop(index)

    for i in range(len(sequence)):
        if sequence[i] <= removed_element:
            sequence[i] += removed_element
        else:
            sequence[i] -= removed_element

    return removed_element


sequence = list(map(int, input().split()))
total_removed_value = 0

while sequence:
    index = int(input())
    removed_value = catch_pokemon(sequence, index)
    total_removed_value += removed_value

print(total_removed_value)
