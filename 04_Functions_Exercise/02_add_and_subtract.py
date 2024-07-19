def sum_numbers(a, b):
    sum_result = a + b
    return sum_result


def subtract(result, c):
    return result - c


def add_and_subtract(a, b, c):
    result = sum_numbers(a, b)
    final_result = subtract(result, c)
    return final_result


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))
