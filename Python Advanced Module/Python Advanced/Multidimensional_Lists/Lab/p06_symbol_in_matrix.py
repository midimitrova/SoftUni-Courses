size = int(input())

matrix = []

for _ in range(size):
    sub_string = list(input())
    matrix.append(sub_string)

symbol = input()
is_found = False

for row in range(size):
    for col in range(size):
        if matrix[row][col] == symbol:
            print(f'({row}, {col})')
            is_found = True
            break
    if is_found:
        break

if not is_found:
    print(f'{symbol} does not occur in the matrix')