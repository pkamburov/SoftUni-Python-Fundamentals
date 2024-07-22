from math import ceil

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())

free_packages = students // 5

total_cost = apron_price * ceil(students + students * 0.2) +\
             egg_price * 10 * students + \
             flour_price * (students - free_packages)


if total_cost <= budget:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    money_needed = total_cost - budget
    print(f"{money_needed:.2f}$ more needed.")
