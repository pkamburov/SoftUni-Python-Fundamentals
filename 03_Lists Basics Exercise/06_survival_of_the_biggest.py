list_of_integers = input().split()
n = int(input())
list_as_integers = [int(x) for x in list_of_integers]

for i in range(n):
    min_num = min(list_as_integers)
    list_as_integers.remove(min_num)

print(", ".join(map(str, list_as_integers)))
