number = input()

digits = []

for digit in number:
    digits.append(digit)

digits.sort()
reversed_digits = digits[::-1]
print(''.join(reversed_digits))

