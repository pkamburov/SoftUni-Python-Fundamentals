operator = input()
first_number = int(input())
second_number = int(input())

def calculate(first_number, second_number, operator):
    if operator == "multiply":
        return first_number * second_number
    elif operator == "divide":
        return int(first_number / second_number)
    elif operator == "add":
        return first_number + second_number
    elif operator == "subtract":
        return first_number - second_number

result = calculate(first_number, second_number, operator)

print(result)
