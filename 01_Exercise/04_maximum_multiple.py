divisor = int(input())
boundary = int(input())

max_number = ''

for i in range(boundary, divisor - 1, -1):
    if i % divisor == 0:
        break

print(i)
