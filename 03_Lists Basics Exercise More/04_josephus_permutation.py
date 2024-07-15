list_of_people = input().split(' ')
k = int(input())

list_of_people = [int(person) for person in list_of_people]
result = []
index = 0

while list_of_people:
    index = (index + k - 1) % len(list_of_people)
    executed = list_of_people.pop(index)
    result.append(executed)

print(f"[{','.join(map(str, result))}]")
