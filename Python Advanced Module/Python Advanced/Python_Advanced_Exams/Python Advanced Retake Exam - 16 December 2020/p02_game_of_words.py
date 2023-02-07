given_string = input()
size = int(input())

player_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

matrix = []
for row in range(size):
    matrix.append(list(input()))

    if 'P' in matrix[row]:
        player_pos = [row, matrix[row].index('P')]
        matrix[row][player_pos[1]] = '-'

movements = int(input())
while movements > 0:
    matrix[player_pos[0]][player_pos[1]] = '-'

    direction = input()

    row = player_pos[0] + directions[direction][0]
    col = player_pos[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        if given_string:
            given_string = given_string[:-1]
            movements -= 1
            matrix[player_pos[0]][player_pos[1]] = 'P'
        continue

    player_pos = [row, col]
    position = matrix[row][col]

    if position.isalpha():
        given_string = given_string + position
        matrix[row][col] = 'P'

    movements -= 1

print(given_string)
[print(*row, sep='') for row in matrix]
