size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split(', ')])

primary_diagonal = []
secondary_diagonal = []

for idx in range(size):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][size - idx - 1])

print(f'Primary diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}')
