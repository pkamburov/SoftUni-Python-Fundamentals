sequence_of_numbers = list(map(int, input().split(' ')))

middle = len(sequence_of_numbers) // 2
left_car = sequence_of_numbers[0:middle]
right_car = sequence_of_numbers[middle + 1:]

left_time = 0
right_time = 0

for i in left_car:
    if i == 0:
        left_time -= left_time * 0.2
    else:
        left_time += i

for i in right_car:
    if i == 0:
        right_time -= right_time * 0.2
    else:
        right_time += i

if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")
else:
    print(f"The winner is right with total time: {right_time:.1f}")
