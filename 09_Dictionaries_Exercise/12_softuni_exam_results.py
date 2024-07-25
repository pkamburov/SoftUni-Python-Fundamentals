students = {}
courses = {}

while True:
    entry_data = input()
    if entry_data == "exam finished":
        break

    parts = entry_data.split('-')
    student, command = parts[0], parts[1]

    if 'banned' in parts:
        if student in students:
            del students[student]
    else:
        language = parts[1]
        points = int(parts[2])

        if student in students:
            if points > students[student]['points']:
                students[student]['points'] = points
            else:
                students[student] = {'language': language, 'points': points}
                if language not in courses:
                    courses[language] = 0
                courses[language] += 1


print("Results:")
for student, data in students.items():
    print(f"{student} | {data['points']}")

print("Submissions:")
for language, count in courses.items():
    print(f"{language} - {count}")
