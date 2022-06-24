import math
import sys

n = int(input())

max_number = -sys.maxsize
total_sum = 0

for i in range(1, n + 1):
    number = int(input())
    if number > max_number:
        max_number = number
    total_sum += number

total_sum -= max_number

diff = math.fabs(total_sum - max_number)

if total_sum == max_number:
    print(f"Yes\nSum = {math.ceil(total_sum)}")
else:
    print(f"No\nDiff = {math.ceil(diff)}")