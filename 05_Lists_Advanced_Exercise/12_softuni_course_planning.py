def add_lesson(title):
    if title not in schedule:
        schedule.append(title)


def insert_lesson(title, index):
    index = int(index)
    if title not in schedule:
        schedule.insert(index, title)


def remove_lesson(title):
    if title in schedule:
        schedule.remove(title)
        exercise_title = f"{lesson_title}-Exercise"
        if exercise_title in schedule:
            schedule.remove(exercise_title)


def swap(title1, title2):
    if title1 and title2 in schedule:
        title1_index = schedule.index(title1)
        title2_index = schedule.index(title2)
        temp = schedule[title1_index]
        schedule[title1_index] = schedule[title2_index]
        schedule[title2_index] = temp


def exercise(title):
    exercise_title = f"{title}-Exercise"
    if title in schedule and exercise_title not in schedule:
        index = schedule.index(title)
        schedule.insert(index + 1, exercise_title)
    elif title not in schedule and exercise_title not in schedule:
        schedule.insert(len(schedule), title)
        schedule.insert(len(schedule), exercise_title)


schedule = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break

    split_command = command.split(":")
    action = split_command[0]
    lesson_title = split_command[1]

    if action == "Add":
        add_lesson(lesson_title)
    elif action == "Insert":
        i = split_command[2]
        insert_lesson(lesson_title, i)
    elif action == "Remove":
        remove_lesson(lesson_title)
    elif action == "Swap":
        current_lesson = split_command[2]
        swap(lesson_title, current_lesson)
        if current_lesson == "Databases" and f"{current_lesson}-Exercise" in schedule:
            exercise_index = schedule.index(f"{current_lesson}-Exercise")
            database_index = schedule.index(current_lesson)
            last_index = schedule[exercise_index]
            schedule.insert(database_index + 1, last_index)
            schedule.pop()

    elif action == "Exercise":
        exercise(lesson_title)

count = 1
for lessons in schedule:
    print(f"{count}.{lessons}")
    count += 1
