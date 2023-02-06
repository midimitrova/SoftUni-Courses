from math import floor

size = int(input())

matrix = []
my_pos = []
my_path = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

target_collected_coins = 100
collected_coins = 0
win_game = False

for row in range(size):
    matrix.append(input().split())

    if 'P' in matrix[row]:
        my_pos = [row, matrix[row].index('P')]
        my_path.append(my_pos)
        matrix[row][my_pos[1]] = '0'

while True:

    if collected_coins >= target_collected_coins:
        win_game = True
        break

    direction = input()

    if not direction:
        break

    row = my_pos[0] + directions[direction][0]
    col = my_pos[1] + directions[direction][1]

    if row < 0:
        row = len(matrix) - 1
    elif row >= size:
        row = 0
    elif col < 0:
        col = len(matrix) - 1
    elif col >= size:
        col = 0

    my_pos = [row, col]
    my_path.append(my_pos)
    position = matrix[row][col]

    if position == 'X':
        collected_coins = floor(collected_coins / 2)
        win_game = False
        break
    elif position.isdigit():
        collected_coins += int(position)
        matrix[my_pos[0]][my_pos[1]] = '0'

if win_game:
    print(f"You won! You've collected {collected_coins} coins.")
else:
    print(f"Game over! You've collected {collected_coins} coins.")

print("Your path:")
[print(row) for row in my_path]