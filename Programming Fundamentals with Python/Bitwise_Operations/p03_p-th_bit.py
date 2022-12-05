num = int(input())
pos = int(input())
binary = []

while num > 0:
    result = num % 2
    binary.append(result)
    num //= 2

while True:
    if len(binary) == 16:
        break
    binary.append(0)

on_pos = binary[pos]
print(on_pos)