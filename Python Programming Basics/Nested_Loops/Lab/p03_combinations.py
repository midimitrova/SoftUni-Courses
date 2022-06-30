n = int(input())
cnt = 0

for x1 in range(0, n + 1):
    for x2 in range(0, n + 1):
        for x3 in range(0, n + 1):
           if n == x1 + x2 + x3:
            cnt += 1

print(cnt)