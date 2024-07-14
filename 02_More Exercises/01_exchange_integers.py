first_integer = int(input())
second_integer = int(input())

print(f'Before: \n'
      f'a = {first_integer} \n'
      f'b = {second_integer}')

first_integer, second_integer = second_integer, first_integer
print(f'After: \n'
      f'a = {first_integer} \n'
      f'b = {second_integer}')
