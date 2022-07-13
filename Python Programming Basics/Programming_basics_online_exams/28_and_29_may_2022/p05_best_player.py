
best_player = ""
max_goals = 0
is_hettrick = False



name = input()
while name != "END":
    number_goals = int(input())

    if number_goals >= 3:
        is_hettrick = True

    if number_goals > max_goals:
        max_goals = number_goals
        best_player = name
    else:
        number_goals

    if number_goals >= 10:
        break

    name = input()

print(f"{best_player} is the best player!")

if is_hettrick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {number_goals} goals.")