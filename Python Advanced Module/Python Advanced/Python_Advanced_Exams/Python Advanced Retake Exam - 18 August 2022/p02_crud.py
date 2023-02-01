size = 6

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

matrix = []
for row in range(size):
    matrix.append(input().split())

first_position = input()
start_position = []
for data in first_position:
    if data.isdigit():
        start_position.append(int(data))

while True:
    command_data = input()
    if command_data == 'Stop':
        break

    current_command = command_data.split(', ')
    command = current_command[0]

    if command == 'Create':
        direction = current_command[1]
        value = current_command[2]

        row = start_position[0] + directions[direction][0]
        col = start_position[1] + directions[direction][1]

        if not (0 <= row < size and 0 <= col < size):
            break

        position = matrix[row][col]
        last_position = [row, col]

        if position == '.':
            matrix[row][col] = value

    elif command == 'Update':
        direction = current_command[1]
        value = current_command[2]

        row = start_position[0] + directions[direction][0]
        col = start_position[1] + directions[direction][1]

        if not (0 <= row < size and 0 <= col < size):
            break

        position = matrix[row][col]
        last_position = [row, col]

        if position != '.':
            matrix[row][col] = value

    elif command == 'Delete':
        direction = current_command[1]

        row = start_position[0] + directions[direction][0]
        col = start_position[1] + directions[direction][1]

        if not (0 <= row < size and 0 <= col < size):
            break

        position = matrix[row][col]
        last_position = [row, col]

        if position != '.':
            matrix[row][col] = '.'

    elif command == 'Read':
        direction = current_command[1]

        row = start_position[0] + directions[direction][0]
        col = start_position[1] + directions[direction][1]

        if not (0 <= row < size and 0 <= col < size):
            break

        position = matrix[row][col]
        last_position = [row, col]

        if position != '.':
            print(position)

    start_position = last_position

[print(*row, sep=' ') for row in matrix]
