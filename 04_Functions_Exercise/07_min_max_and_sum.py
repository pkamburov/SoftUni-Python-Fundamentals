def min_max_sum(a):
    numbers = [int(number) for number in a]
    min_number = min(numbers)
    max_number = max(numbers)
    sum_number = sum(numbers)
    return f"The minimum number is {min_number}" \
           f"\nThe maximum number is {max_number}" \
           f"\nThe sum number is: {sum_number}"


sequence = input().split()
print(min_max_sum(sequence))
