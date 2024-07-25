companies = {}

while True:
    command = input()
    if command == 'End':
        break

    company_name, employee_id = command.split(' -> ')

    if company_name not in companies:
        companies[company_name] = []

    if employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)

for company_name, employees in companies.items():
    print(f'{company_name}')
    for employee_id in employees:
        print(f'-- {employee_id}')
