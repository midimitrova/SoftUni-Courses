import os

while True:
    line = input()

    if line == 'End':
        break

    command = line.split('-')

    if command[0] == 'Create':
        file_name = command[1]

        file = open(file_name, 'w')
        file.close()

    elif command[0] == 'Add':
        file_name, content = command[1:]
        try:
            with open(file_name, 'a') as file:
                file.writelines(content + '\n')
        except FileExistsError:
            with open(file_name, 'a') as file:
                file.writelines(content + '\n')

    elif command[0] == 'Replace':
        file_name, old_string, new_string = command[1:]
        try:
            with open(file_name) as file:
                file_data = file.read()
            file_data = file_data.replace(old_string, new_string)

            with open(file_name, 'w') as file:
                file.write(file_data)

        except FileNotFoundError:
            print("An error occurred")

    elif command[0] == 'Delete':
        file_name = command[1]
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")
