def is_outside(row, col, size):
    return 0 > row or 0 > col or row >= size or col >= size


size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input().split()
    if command[0] == 'END':
        break
    row, col, value = [int(x) for x in command[1:]]

    if is_outside(row, col, size):
        print('Invalid coordinates')
        continue
    if command[0] == 'Add':
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

for row in range(size):
    print(*matrix[row], end='\n')