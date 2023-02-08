def check_cell_value(some_row, some_col, bombs, some_size, some_moves):
    value = 0
    for way in some_moves.values():
        cell_row = some_row + way[0]
        cell_col = some_col + way[1]
        if 0 <= cell_row < some_size and 0 <= cell_col < some_size:
            if [cell_row, cell_col] in bombs:
                value += 1
    return value


size = int(input())
bombs_number = int(input())
bombs_location = [list(map(int, input()[1:-1].split(','))) for bomb in range(bombs_number)]

moves = {'u': (-1, 0), 'ul': (-1, -1), 'ur': (-1, 1),
         'd': (1, 0), 'dl': (1, -1), 'dr': (1, 1),
         'l': (0, -1), 'r': (0, 1)}

matrix = []

for row in range(size):
    current_row = []
    for col in range(size):
        cell = 0
        if [row, col] in bombs_location:
            cell = '*'
        else:
            cell = check_cell_value(row, col, bombs_location, size, moves)
        current_row.append(cell)
    matrix.append(current_row)

print('\n'.join(' '.join(map(str, row)) for row in matrix))