number = int(input())
binary_digit = int(input())
counter_digit = 0

while number > 0:

    remainder = number % 2
    if remainder == binary_digit:
        counter_digit += 1
    number //= 2

print(counter_digit)
