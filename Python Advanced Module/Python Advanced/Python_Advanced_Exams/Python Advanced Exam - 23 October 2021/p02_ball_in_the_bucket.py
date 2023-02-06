import sys

size = 6

matrix = []

throw = 3
sum_points_col = 0
catalogue = {
    'Football': [100, 199],
    'Teddy Bear': [200, 299],
    'Lego Construction Set': [300, sys.maxsize],
}


for row in range(size):
    matrix.append([int(x) if x.isdigit() else x for x in input().split()])

while throw > 0:

    row, col = list(map(int, input()[1:-1].split(', ')))

    if not (0 <= row < size and 0 <= col < size):
        throw -= 1
        continue

    position = matrix[row][col]

    if position == 'B':
        matrix[row][col] = 0
        for x in matrix:
            sum_points_col += x[col]

    throw -= 1


if sum_points_col < 100:
    needed_points = 100 - sum_points_col
    print(f'Sorry! You need {needed_points} points more to win a prize.')
else:
    for gift, points in catalogue.items():
        if points[0] <= sum_points_col <= points[1]:
            print(f"Good job! You scored {sum_points_col} points, and you've won {gift}.")
            break

