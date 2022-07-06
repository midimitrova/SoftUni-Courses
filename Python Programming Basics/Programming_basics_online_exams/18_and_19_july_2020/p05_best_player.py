

max_goals = 0

het_trick = False
best_player = ""

name = input()
while True:
    if name == "END":
        break

    number_goals = int(input())

    if number_goals > max_goals:
        max_goals = number_goals
        best_player = name


    if number_goals >= 3:
        het_trick = True


    if number_goals >= 10:
        break

    name = input()

print(f"{best_player} is the best player!")
if het_trick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")

