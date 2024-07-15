fire_cells = input().split("#")
water = int(input())
effort = 0
total_fire_put_out = 0
cells_to_put_out = []

for cell in fire_cells:
    info = cell.split(" = ")
    fire_type = info[0]
    cell_value = int(info[1])
    if fire_type == "Low" and water >= cell_value:
        if 0 < cell_value <= 50:
            water -= cell_value
            effort += 0.25 * cell_value
            total_fire_put_out += cell_value
            cells_to_put_out.append(cell_value)
    elif fire_type == "Medium" and water >= cell_value:
        if 50 < cell_value <= 80:
            water -= cell_value
            effort += 0.25 * cell_value
            total_fire_put_out += cell_value
            cells_to_put_out.append(cell_value)
    elif fire_type == "High" and water >= cell_value:
        if 80 < cell_value <= 125:
            water -= cell_value
            effort += 0.25 * cell_value
            total_fire_put_out += cell_value
            cells_to_put_out.append(cell_value)

print("Cells:")
for each_cell in cells_to_put_out:
    print(f" - {each_cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire_put_out}")
