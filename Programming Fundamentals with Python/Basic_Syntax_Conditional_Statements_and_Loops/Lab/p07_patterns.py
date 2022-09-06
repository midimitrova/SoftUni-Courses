n = int(input())

for row1 in range(1, n + 1):
    print('*' * row1)
for row2 in range(n - 1, 0, -1):
    print('*' * row2)