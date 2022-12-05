num = int(input())
binary = []

while num > 0:
    result = num % 2
    binary.append(result)
    num //= 2

on_pos_1 = int(binary[1])
print(on_pos_1)