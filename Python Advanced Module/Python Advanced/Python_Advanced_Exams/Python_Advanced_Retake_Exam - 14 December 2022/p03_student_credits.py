def students_credits(*args):
    student_info = {}
    total_credits = 0
    needed_credits = 240
    for data_info in args:
        data = data_info.split('-')
        course_name = data[0]
        credit = int(data[1])
        max_test_points = int(data[2])
        student_points = int(data[3])
        credits_student_get = credit * (student_points / max_test_points)
        student_info[course_name] = credits_student_get
        total_credits += credits_student_get

    sorted_data = sorted(student_info.items(), key=lambda x: -x[1])

    result = ''
    if total_credits >= needed_credits:
        result += f'Diyan gets a diploma with {total_credits:.1f} credits.\n'
    else:
        result += f'Diyan needs {(needed_credits - total_credits):.1f} credits more for a diploma.\n'

    for course in sorted_data:
        result += f'{course[0]} - {course[1]:.1f}\n'

    return result






# --- TEST CODE ---
print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)


# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )


# print(
#     students_credits(
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Java Development-10-300-150"
#     )
# )
