input_numbers = input().split()
rounded_numbers = []

for i in input_numbers:
    i = float(i)
    rounded_numbers.append(round(i))

print(rounded_numbers)
