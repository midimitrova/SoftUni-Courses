n = int(input())

student_data = {}

while n > 0:
    name, grade = input().split()
    grade = float(grade)

    if name not in student_data:
        student_data[name] = []
    student_data[name].append(grade)

    n -= 1

for name, grades in student_data.items():
    print(f'{name} -> {" ".join([f"{el:.2f}" for el in grades])} (avg: {sum(grades) / len(grades):.2f})')
