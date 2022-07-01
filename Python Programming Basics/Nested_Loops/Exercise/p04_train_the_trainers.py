n = int(input())


cnt = 0
grades = 0
grades_cnt = 0

for presentations in range(1, n + 1):
    presentation = input()
    while presentation != "Finish":
        total_grade = 0
        while n > cnt:
            cnt += 1
            grade = float(input())
            total_grade += grade

        grades += total_grade
        grades_cnt += cnt
        cnt = 0
        print(f"{presentation} - {(total_grade / n):.2f}.")

        presentation = input()

    print(f"Student's final assessment is {(grades / grades_cnt):.2f}.")
    break


