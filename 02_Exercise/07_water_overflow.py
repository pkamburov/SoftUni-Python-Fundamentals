number_of_lines = int(input())
liters = 0

for pours in range(number_of_lines):
    current_pour = int(input())
    if current_pour + liters > 255:
        print("Insufficient capacity!")
    else:
        liters += current_pour

print(liters)
