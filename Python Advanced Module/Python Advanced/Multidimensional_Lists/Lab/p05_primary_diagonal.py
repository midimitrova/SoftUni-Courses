size = int(input())

matrix = []

for _ in range(size):
    sub_matrix = [int(x) for x in input().split()]
    matrix.append(sub_matrix)

total = 0
for row in range(size):
    total += matrix[row][row]

print(total)


