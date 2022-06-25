number_students = int(input())

grade1 = 0
grade2 = 0
grade3 = 0
grade4 = 0
total_grade = 0

for grade in range(1, number_students + 1):
    grade_from_exam = float(input())
    if grade_from_exam <= 2.99:
        grade1 += 1
        total_grade += grade_from_exam
    elif grade_from_exam <= 3.99:
        grade2 += 1
        total_grade += grade_from_exam
    elif grade_from_exam <= 4.99:
        grade3 += 1
        total_grade += grade_from_exam
    elif grade_from_exam >= 5:
        grade4 += 1
        total_grade += grade_from_exam

average_grade = total_grade / number_students

print(f"Top students: {(grade4 / number_students) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {(grade3 / number_students) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {(grade2 / number_students) * 100:.2f}%")
print(f"Fail: {(grade1 / number_students) * 100:.2f}%")

print(f"Average: {average_grade:.2f}")

