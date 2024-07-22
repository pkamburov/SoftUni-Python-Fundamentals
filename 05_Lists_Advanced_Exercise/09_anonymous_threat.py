text = input().split()
command = input().split()

while command[0] != "3:1":
    if command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(text) - 1:
            end_index = len(text) - 1
        merged_elements = "".join(text[start_index:end_index+1])
        text[start_index:end_index+1] = [merged_elements]
    elif command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])
        element = text[index]
        divided_partition = []
        partition_length = len(element) // partitions
        for current_element in range(partitions):
            if current_element != partitions - 1:
                divided_partition.append(
                    element[current_element * partition_length: (current_element + 1) * partition_length])
            else:
                divided_partition.append(element[current_element * partition_length:])
        text[index:index+1] = divided_partition

    command = input().split()
print(" ".join(text))
