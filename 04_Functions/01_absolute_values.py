sequence = input().split()

numbers = []

for i in sequence:
    number = float(i)
    numbers.append(number)

absolutes = []
for n in numbers:
    absolute_number = abs(n)
    absolutes.append(absolute_number)

print(absolutes)
