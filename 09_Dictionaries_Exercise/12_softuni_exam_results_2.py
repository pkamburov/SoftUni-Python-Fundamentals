results = {}
submissions = {}

while True:
    command = input()
    if command == 'exam finished':
        break

    if 'banned' in command:
        username, command = command.split('-')
        if username in results.keys():
            del results[username]
        continue

    username, language, points = command.split('-')
    points = int(points)

    if username in results.keys():
        submissions[language] += 1
        if points > results[username]:
            results[username] = points
    else:
        results[username] = points
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

print("Results:")
for result, points in results.items():
    print(f"{result} | {points}")
print("Submissions:")
for submission, counter in submissions.items():
    print(f"{submission} - {counter}")
