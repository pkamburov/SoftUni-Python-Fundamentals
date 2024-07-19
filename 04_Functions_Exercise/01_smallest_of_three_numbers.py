def smallest(numbers: list):
    return min(numbers)


first_int = int(input())
second_int = int(input())
third_int = int(input())

smallest_element = smallest([first_int, second_int, third_int])
print(smallest_element)
