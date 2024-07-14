number_of_lines = int(input())
opening_counter = 0
closing_counter = 0
opened = False

for i in range(number_of_lines):
    key = input()
    if key == '(':
        opening_counter += 1
        if opened is True:
            break
        opened = True
    elif key == ')':
        closing_counter += 1
        if opened is False:
            break
        opened = False

if opening_counter != closing_counter:
    print('UNBALANCED')
else:
    print('BALANCED')
