courses = {}

while True:
    input_data = input()

    if input_data == 'end':
        break

    course, student_name = input_data.split(' : ')

    if course not in courses.keys():
        courses[course] = []

    courses[course].append(student_name)

for course, registered_students in courses.items():
    print(f"{course}: {len(registered_students)}")
    for student_name in registered_students:
        print(f"-- {student_name}")
