rows = int(input())

matrix = []

for _ in range(rows):
    sub_matrix = [int(x) for x in input().split(', ')]
    matrix.extend(sub_matrix)

print(matrix)