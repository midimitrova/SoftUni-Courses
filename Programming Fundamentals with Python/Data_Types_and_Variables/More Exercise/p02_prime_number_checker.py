from math import ceil

number = int(input())

is_prime = True
for div in range(2, ceil(number / 2) + 1):
    if number % div == 0:
        is_prime = False
        break

if is_prime:
    print("True")
else:
    print("False")