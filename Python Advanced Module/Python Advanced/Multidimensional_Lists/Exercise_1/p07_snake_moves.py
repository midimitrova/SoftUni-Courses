rows, cols = [int(x) for x in input().split()]
word = input()


idx = 0
for row in range(rows):
    rows_elements = []
    for col in range(cols):
        rows_elements.append(word[idx % len(word)])
        idx += 1
    if row % 2 == 0:
        print(*rows_elements, sep='')
    else:
        print(*reversed(rows_elements), sep='')