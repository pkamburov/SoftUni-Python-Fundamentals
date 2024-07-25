rows = int(input())
students = {}

for i in range(rows):
    student_name = input()
    student_grade = float(input())

    if student_name not in students:
        students[student_name] = []
    students[student_name].append(student_grade)

for student, grades in students.items():
    average_grade = sum(grades) / len(grades)
    students[student] = average_grade

for name, average_grade in students.items():
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
