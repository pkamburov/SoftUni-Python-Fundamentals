number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_attendances = 0

for student in range(number_of_students):
    attendance_count = int(input())
    total_bonus = round((attendance_count / number_of_lectures) * (5 + additional_bonus))
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_attendances = attendance_count


print(f'Max Bonus: {max_bonus}.\n'
      f'The student has attended {max_attendances} lectures.')
