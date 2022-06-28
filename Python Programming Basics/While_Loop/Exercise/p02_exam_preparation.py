failed_times = int(input())

fail_grade_cnt = 0
grade_cnt = 0
total_grade = 0
last_problem = ""

while True:
    name = input()

    if name == "Enough":
        print(f"Average score: {total_grade / grade_cnt:.2f}")
        print(f"Number of problems: {grade_cnt}")
        print(f"Last problem: {last_problem}")
        break

    grade = int(input())

    grade_cnt += 1
    total_grade += grade

    if grade <= 4:
        fail_grade_cnt += 1
        if fail_grade_cnt >= failed_times:
            print(f"You need a break, {fail_grade_cnt} poor grades.")
            break

    last_problem = name


