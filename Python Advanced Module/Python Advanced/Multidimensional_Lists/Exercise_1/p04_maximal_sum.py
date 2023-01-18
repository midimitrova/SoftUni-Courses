from sys import maxsize

rows, cols = [int(x) for x in input().split()]

matrix = []

max_sum = -maxsize
biggest_square = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for row in range(rows - 2):
    for col in range(cols - 2):
        first_row = [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]]
        second_row = [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]]
        third_row = [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
        current_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if current_sum > max_sum:
            biggest_square.clear()
            biggest_square.append(first_row)
            biggest_square.append(second_row)
            biggest_square.append(third_row)
            max_sum = current_sum

if biggest_square:
    print(f'Sum = {max_sum}')
    [print(*biggest_square[row]) for row in range(3)]

