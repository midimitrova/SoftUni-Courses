rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for col in range(cols):
    result = 0
    for row in range(rows):
        result += matrix[row][col]

    print(result)
