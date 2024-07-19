def sorted_list(some_list):
    numbers = [int(number) for number in some_list]
    return sorted(numbers)


sequence = input().split()
print(sorted_list(sequence))
