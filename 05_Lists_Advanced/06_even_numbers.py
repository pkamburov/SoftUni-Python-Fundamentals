number_list = list(map(int, input().split(", ")))

indices_or_no = map(lambda x: x if number_list[x] % 2 == 0 else 'no', range(len(number_list)))

even_indices = list(filter(lambda a: a != 'no', indices_or_no))
print(even_indices)
