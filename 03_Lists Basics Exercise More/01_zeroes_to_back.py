integers = list(map(int, input().split(', ')))

for i in integers:
    if i == 0:
        integers.remove(i)
        integers.append(i)

print(integers)
