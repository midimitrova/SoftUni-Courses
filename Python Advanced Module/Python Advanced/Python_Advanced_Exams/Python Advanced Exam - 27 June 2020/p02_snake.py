size = int(input())

matrix = []
food = 0
tunel_coord = set()
start_position = []
last_position = []

directions = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0),
}

for row in range(size):
    matrix.append(list(input()))

    if 'S' in matrix[row]:
        start_position = [row, matrix[row].index('S')]
        matrix[row][start_position[1]] = '.'

    if 'B' in matrix[row]:
        tunel_coord.add((row, matrix[row].index('B')))

while True:
    if food >= 10:
        print("You won! You fed the snake.")
        matrix[start_position[0]][start_position[1]] = "S"
        break

    direction = input()

    row = start_position[0] + directions[direction][0]
    col = start_position[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        print("Game over!")
        break

    position = matrix[row][col]
    last_position = [row, col]

    if position == 'B':
        current_tunnel = {(row, col)}
        second_tunnel = tunel_coord.difference(current_tunnel)

        matrix[row][col] = "."
        last_position = second_tunnel.pop()

    elif position == '*':
        food += 1
        matrix[last_position[0]][last_position[1]] = "."

    matrix[last_position[0]][last_position[1]] = '.'
    start_position = last_position

print(f'Food eaten: {food}')
[print(*row, sep='') for row in matrix]
