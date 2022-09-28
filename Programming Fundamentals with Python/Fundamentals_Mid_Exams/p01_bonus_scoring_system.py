from math import ceil

number_of_students = int(input())
number_of_the_lectures = int(input())
the_additional_bonus = int(input())
max_bonus = 0
best_student_attendance = 0
total_bonus = 0

while number_of_students > 0:
    attendance_of_each_student = int(input())

    total_bonus = attendance_of_each_student / number_of_the_lectures * (5 + the_additional_bonus)

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        best_student_attendance = attendance_of_each_student

    number_of_students -= 1

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {ceil(best_student_attendance)} lectures.")