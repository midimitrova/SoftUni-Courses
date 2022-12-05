num = int(input())
pos = int(input())
binary = []

while num > 0:
    result = num % 2
    num //= 2
    binary.append(result)

binary[pos] = 0

while len(binary) < 12:
    binary.append(0)

binary = binary[::-1]
print(f"{''.join(list(map(lambda x: str(x), binary)))}")