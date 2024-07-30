file_path = input().split('\\')
filename_with_extension = file_path[-1]
file_name, extension = filename_with_extension.split('.')

print(f"File name: {file_name}")
print(f"File extension: {extension}")
