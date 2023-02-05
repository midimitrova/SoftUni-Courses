rows, cols = [int(x) for x in input().split(', ')]

matrix = []
my_pos = []
christmas_decorations = 0
gifts = 0
cookies = 0
presents = {
    'Christmas decorations': 0,
    'Gifts': 0,
    'Cookies': 0,
}

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(rows):
    matrix.append(input().split())

    if 'Y' in matrix[row]:
        my_pos = [row, matrix[row].index('Y')]
        matrix[row][my_pos[1]] = 'x'

    if 'D' in matrix[row]:
        christmas_decorations += matrix[row].count('D')

    if 'G' in matrix[row]:
        gifts += matrix[row].count('G')

    if 'C' in matrix[row]:
        cookies += matrix[row].count('C')

are_collected = False
commands = input()
while commands != 'End':

    direction, steps = commands.split('-')
    steps = int(steps)

    for step in range(1, steps + 1):
        matrix[my_pos[0]][my_pos[1]] = 'x'
        row = my_pos[0] + directions[direction][0]
        col = my_pos[1] + directions[direction][1]

        if row < 0:
            row = rows - 1
        elif row >= rows:
            row = 0
        elif col < 0:
            col = cols - 1
        elif col >= cols:
            col = 0

        my_pos = [row, col]
        position = matrix[row][col]

        if position == 'D':
            christmas_decorations -= 1
            presents['Christmas decorations'] += 1
        elif position == 'G':
            gifts -= 1
            presents['Gifts'] += 1
        if position == 'C':
            cookies -= 1
            presents['Cookies'] += 1
        matrix[my_pos[0]][my_pos[1]] = 'Y'
        if cookies == 0 and gifts == 0 and christmas_decorations == 0:
            print('Merry Christmas!')
            are_collected = True
            break

    if are_collected:
        break
    commands = input()

print('You\'ve collected:')
for present, value in presents.items():
    print(f'- {value} {present}')
[print(*row) for row in matrix]
