sequence = input().split()
some_string = input()

message = []

for number in sequence:
    index_sum = sum(map(int, number))

    while index_sum >= len(some_string):
        index_sum -= len(some_string)

    message.append(some_string[index_sum])
    some_string = some_string[:index_sum] + some_string[index_sum + 1:]

print("".join(message))
