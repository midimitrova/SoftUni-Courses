size = int(input())
racing_number = input()

covered_distance = 0
matrix = []
tunel_coord = set()
start_position = (0, 0)
last_position = set()

directions = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0),
}

for row in range(size):
    matrix.append(input().split())

    if 'T' in matrix[row]:
        tunel_coord.add((row, matrix[row].index('T')))

while True:

    direction = input()

    if direction == 'End':
        matrix[start_position[0]][start_position[1]] = "C"
        print(f'Racing car {racing_number} DNF.')
        break

    row = start_position[0] + directions[direction][0]
    col = start_position[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    position = matrix[row][col]
    last_position = (row, col)

    if position == 'T':
        current_tunnel = {(row, col)}
        second_tunnel = tunel_coord.difference(current_tunnel)

        matrix[row][col] = "."
        last_position = second_tunnel.pop()
        covered_distance += 30

    elif position == '.':
        covered_distance += 10

    elif position == 'F':
        covered_distance += 10
        print(f'Racing car {racing_number} finished the stage!')
        matrix[last_position[0]][last_position[1]] = "C"
        break

    matrix[last_position[0]][last_position[1]] = '.'
    start_position = last_position

print(f'Distance covered {covered_distance} km.')
[print(*row, sep='') for row in matrix]
