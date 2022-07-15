import math

n = int(input())

total_sum = 0
max_num = 0

for i in range(0, n):
    number = int(input())
    if number > max_num:
        max_num = number
        total_sum += number


total_sum -= max_num

diff = math.fabs(total_sum - max_num)

if total_sum == max_num:
    print(f"Yes, sum = {max_num}")
else:
    print(f"No, diff = {diff}")


