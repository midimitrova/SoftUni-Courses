number_moves = int(input())

total_points = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0

for num in range(1, number_moves + 1):
    curr_number = int(input())

    if 0 <= curr_number <= 9:
        num1 = curr_number * 20/100
        total_points += num1
        p1 += 1
    elif 10 <= curr_number <= 19:
        num2 = curr_number * 30/100
        total_points += num2
        p2 += 1
    elif 20 <= curr_number <= 29:
        num3 = curr_number * 40/100
        total_points += num3
        p3 += 1
    elif 30 <= curr_number <= 39:
        num4 = 50
        total_points += num4
        p4 += 1
    elif 40 <= curr_number <= 50:
        num5 = 100
        total_points += num5
        p5 += 1
    elif 0 > curr_number or curr_number > 50:
        num6 = total_points / 2
        total_points = num6
        p6 += 1

print(f"{total_points:.2f}")
print(f"From 0 to 9: {(p1 / number_moves) * 100:.2f}%")
print(f"From 10 to 19: {(p2 / number_moves) * 100:.2f}%")
print(f"From 20 to 29: {(p3 / number_moves) * 100:.2f}%")
print(f"From 30 to 39: {(p4 / number_moves) * 100:.2f}%")
print(f"From 40 to 50: {(p5 / number_moves) * 100:.2f}%")
print(f"Invalid numbers: {(p6 / number_moves) * 100:.2f}%")