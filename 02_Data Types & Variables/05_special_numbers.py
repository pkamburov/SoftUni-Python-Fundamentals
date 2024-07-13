n = int(input())

special = False

for number in range(1, n + 1):
    current_number_as_string = str(number)
    digits_sum = 0
    special = False
    for digit in current_number_as_string:
        digits_sum += int(digit)
    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        special = True
    print(f'{number} -> {special}')
