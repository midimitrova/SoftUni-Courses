from collections import deque

size = 6

matrix = []
rover_pos = []

water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if 'E' in matrix[row]:
        rover_pos = [row, matrix[row].index('E')]

direction_commands = deque(input().split(', '))

while len(direction_commands) > 0:

    current_direction = direction_commands.popleft()

    row = rover_pos[0] + directions[current_direction][0]
    col = rover_pos[1] + directions[current_direction][1]

    if row < 0:
        row = len(matrix) - 1
    elif row >= size:
        row = 0
    elif col < 0:
        col = len(matrix) - 1
    elif col >= size:
        col = 0

    rover_pos = [row, col]
    position = matrix[row][col]

    if position == 'W':
        water_deposit += 1
        print(f'Water deposit found at {row, col}')
    elif position == 'M':
        metal_deposit += 1
        print(f'Metal deposit found at {row, col}')
    elif position == 'C':
        concrete_deposit += 1
        print(f'Concrete deposit found at {row, col}')
    elif position == 'R':
        print(f'Rover got broken at {row, col}')
        break

if water_deposit >= 1 and metal_deposit >= 1 and concrete_deposit >= 1:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')
