first_string = input()
second_string = input()

new_string = first_string

for i in range(len(first_string)):
    if first_string[i] != second_string[i]:
        new_string = new_string[:i] + second_string[i] + new_string[i+1:]

    if new_string[i] != first_string[i]:
        print(new_string)
