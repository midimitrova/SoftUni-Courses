size = int(input())

matrix = []
submarine_pos = []
battle_cruisers = 0
hit_mines = 3

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    matrix.append(list(input()))

    if 'S' in matrix[row]:
        submarine_pos = [row, matrix[row].index('S')]
        matrix[row][submarine_pos[1]] = '-'

    if 'C' in matrix[row]:
        battle_cruisers += matrix[row].count('C')

while battle_cruisers and hit_mines:
    direction = input()

    row = submarine_pos[0] + directions[direction][0]
    col = submarine_pos[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    last_coord = []
    submarine_pos = [row, col]
    position = matrix[row][col]
    matrix[row][col] = '-'

    if position == '*':
        hit_mines -= 1
        last_coord.append([row, col])
        matrix[row][col] = '-'

    if position == 'C':
        battle_cruisers -= 1
        last_coord.append([row, col])
        matrix[row][col] = '-'

matrix[submarine_pos[0]][submarine_pos[1]] = 'S'

if battle_cruisers == 0:
    print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
elif hit_mines == 0:
    print(f'Mission failed, U-9 disappeared! Last known coordinates [{last_coord[0][0]}, {last_coord[0][1]}]!')

[print(*row, sep='') for row in matrix]
