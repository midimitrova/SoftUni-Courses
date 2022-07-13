number_students = int(input())
cnt_2 = 0
cnt_3 = 0
cnt_4 = 0
cnt_5 = 0
total_grade = 0

for student in range(1, number_students + 1):
    curr_grade = float(input())
    total_grade += curr_grade

    if curr_grade <= 2.99:
        cnt_2 += 1

    elif curr_grade <= 3.99:
        cnt_3 += 1

    elif curr_grade <= 4.99:
        cnt_4 += 1

    elif curr_grade >= 5:
        cnt_5 += 1


print(f"Top students: {(cnt_5 / number_students) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {(cnt_4 / number_students) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {(cnt_3 / number_students) * 100:.2f}%")
print(f"Fail: {(cnt_2 / number_students) * 100:.2f}%")
print(f"Average: {total_grade / number_students:.2f}")



