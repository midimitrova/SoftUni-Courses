from math import ceil, sqrt

num1 = int(input())
num2 = int(input())
num3 = int(input())



for n1 in range(1, num1 + 1):
    for n2 in range(2, num2 + 1):
        is_prime = True
        for div in range(2, ceil(n2 / 2) + 1):
            if n2 % div == 0:
                is_prime = False
                break

        for n3 in range(1, num3 + 1):
            if n3 % 2 == 0 and n1 % 2 == 0 and is_prime == True:
                print(f"{n1} {n2} {n3}")
