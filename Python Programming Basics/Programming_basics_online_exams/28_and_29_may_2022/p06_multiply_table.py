number = int(input())

hundreds = int(number / 100)
tens = int((number / 10) % 10)
ones = int(number % 10)

for n1 in range(1, ones + 1):
    for n2 in range(1, tens + 1):
        for n3 in range(1, hundreds + 1):
            result = int(n1) * int(n2) * int(n3)
            print(f"{n1} * {n2} * {n3} = {result};")
