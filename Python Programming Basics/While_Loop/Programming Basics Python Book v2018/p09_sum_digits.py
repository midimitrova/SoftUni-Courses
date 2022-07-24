n = int(input())
total_sum = 0

while n > 0:

    last_digit = n % 10
    n = n // 10
    total_sum += last_digit

print(total_sum)