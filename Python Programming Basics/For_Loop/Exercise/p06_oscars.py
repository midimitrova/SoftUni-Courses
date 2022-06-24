name_actor = input()
points_from_academy = float(input())
number_evaluating_people = int(input())

name_lenght = 0
total_points = 0 + points_from_academy
points = 0

for name in range(1, number_evaluating_people + 1):
    name_evaluating = input()
    points_from_evaluating = float(input())

    name_lenght = len(name_evaluating)

    points = ((name_lenght * points_from_evaluating) / 2)

    total_points += points

    if total_points > 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!")
        break

if total_points <= 1250.5:
    print(f"Sorry, {name_actor} you need {1250.5 - total_points:.1f} more!")




