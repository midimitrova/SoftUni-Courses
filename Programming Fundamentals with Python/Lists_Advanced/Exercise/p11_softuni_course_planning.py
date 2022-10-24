lessons = input().split(', ')

command = input()
while command != 'course start':
    command = command.split(':')
    current_command = command[0]
    lesson_title = command[1]

    if current_command == 'Add':
        if lesson_title not in lessons:
            lessons.append(lesson_title)

    elif current_command == 'Insert':
        index = int(command[2])
        if lesson_title not in lessons:
            lessons.insert(index, lesson_title)

    elif current_command == 'Remove':
        exercise_title = f'{lesson_title}-Exercise'
        if lesson_title in lessons:
            lessons.remove(lesson_title)
        if exercise_title in lessons:
            lessons.remove(exercise_title)

    elif current_command == 'Swap':
        lesson_title_one = lesson_title
        lesson_title_two = command[2]
        if lesson_title_one in lessons and \
                lesson_title_two in lessons:
            index_one = lessons.index(lesson_title_one)
            index_two = lessons.index(lesson_title_two)
            first_has_exercise = False
            second_has_exercise = False
            if index_one + 1 in range(len(lessons)):
                first_has_exercise = "Exercise" in lessons[index_one + 1]
            if index_two + 1 in range(len(lessons)):
                second_has_exercise = "Exercise" in lessons[index_two + 1]
            lessons[index_one], lessons[index_two] = lessons[index_two], lessons[index_one]
            if first_has_exercise and second_has_exercise:
                lessons[index_one + 1], lessons[index_two + 1] = lessons[index_two + 1], lessons[index_one + 1]
            elif not first_has_exercise and second_has_exercise:
                lessons.insert(index_one + 1, lessons.pop(index_two + 1))
            elif first_has_exercise and not second_has_exercise:
                lessons.insert(index_two + 1, lessons.pop(index_one + 1))

    elif current_command == 'Exercise':
        exercise_title = f'{lesson_title}-Exercise'
        if lesson_title in lessons and exercise_title not in lessons:
            index_lesson = lessons.index(lesson_title)
            lessons.insert(index_lesson + 1, exercise_title)
        elif lesson_title not in lessons:
            lessons.append(lesson_title)
            lessons.append(exercise_title)

    command = input()

for i in range(len(lessons)):
    print(f'{i + 1}.{lessons[i]}')
