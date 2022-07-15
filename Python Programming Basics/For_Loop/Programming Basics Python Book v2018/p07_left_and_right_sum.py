import  math

n = int(input())
left_sum = 0
right_sum = 0

for i in range(0, n):
    number_left_side = float(input())
    left_sum += number_left_side

for i in range(0, n):
    number_right_side = float(input())
    right_sum += number_right_side

diff = math.fabs(right_sum - left_sum)

if right_sum == left_sum:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {diff}")
