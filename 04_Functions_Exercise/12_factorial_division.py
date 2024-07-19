def calc_factorial(number):
    for current_num in range(1, number):
        number *= current_num
    return number


first_num = int(input())
second_num = int(input())
first_factorial = calc_factorial(first_num)
second_factorial = calc_factorial(second_num)
result = first_factorial / second_factorial
print(f"{result:.2f}")
