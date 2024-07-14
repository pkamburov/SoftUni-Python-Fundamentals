from math import ceil

number_of_persons = int(input())
capacity = int(input())

courses = ceil(number_of_persons / capacity)
print(courses)
