first_employee_per_hour = int(input())
second_employee_per_hour = int(input())
third_employee_per_hour = int(input())
total_students = int(input())

time_needed = 0

while total_students > 0:
    helped_students_per_hour = first_employee_per_hour + second_employee_per_hour + third_employee_per_hour
    time_needed += 1
    if time_needed % 4 == 0:
        continue
    total_students -= helped_students_per_hour

print(f"Time needed: {time_needed}h.")
