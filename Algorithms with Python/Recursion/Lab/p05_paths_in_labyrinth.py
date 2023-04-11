def find_all_paths(row, col, matrix, direction, path):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return

    if matrix[row][col] == '*':
        return

    if matrix[row][col] == 'e':
        path.append(direction)
        print(*path, sep='')
        path.pop()
        return

    if matrix[row][col] == 'v':
        return

    matrix[row][col] = 'v'
    path.append(direction)

    find_all_paths(row - 1, col, matrix, 'U', path)
    find_all_paths(row + 1, col, matrix, 'D', path)
    find_all_paths(row, col - 1, matrix, 'L', path)
    find_all_paths(row, col + 1, matrix, 'R', path)

    matrix[row][col] = '-'
    path.pop()


rows = int(input())
cols = int(input())
matrix = []

for _ in range(rows):
    matrix.append(list(input()))

find_all_paths(0, 0, matrix, '', [])
