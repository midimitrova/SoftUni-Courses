import math

n = int(input())


right_sum = 0
left_sum = 0

for i in range(0, n):
    right_number = int(input())
    right_sum += right_number
for i in range(0, n):
    left_number = int(input())
    left_sum += left_number
diff = math.fabs(right_sum - left_sum)
if right_sum == left_sum:
    print(f"Yes, sum = {math.ceil(right_sum)}")
else:
    print(f"No, diff = {math.ceil(diff)}")
