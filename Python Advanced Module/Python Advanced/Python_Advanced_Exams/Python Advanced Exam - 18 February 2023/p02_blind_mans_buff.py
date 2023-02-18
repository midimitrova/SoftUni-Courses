rows, cols = [int(x) for x in input().split()]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

matrix = []
my_pos = []
players = 0
moves = 0
touched_players = 0


for row in range(rows):
    matrix.append(input().split())

    if 'B' in matrix[row]:
        my_pos = [row, matrix[row].index('B')]
        matrix[row][my_pos[1]] = '-'

    if 'P' in matrix[row]:
        players += matrix[row].count('P')


while True:
    if players == touched_players:
        break

    direction = input()

    if direction == 'Finish':
        break

    row = my_pos[0] + directions[direction][0]
    col = my_pos[1] + directions[direction][1]

    if not (0 <= row < rows and 0 <= col < cols):
        continue

    position = matrix[row][col]
    last_position = [row, col]

    if position == 'O':
        continue

    elif position == 'P':
        touched_players += 1
        matrix[last_position[0]][last_position[1]] = "-"

    moves += 1
    my_pos = last_position

print("Game over!")
print(f"Touched opponents: {touched_players} Moves made: {moves}")