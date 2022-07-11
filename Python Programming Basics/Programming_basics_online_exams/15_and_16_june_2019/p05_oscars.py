name_actor = input()
points_from_academy = float(input())
number_evaluate_people = int(input())

points = 0
total_points = 0 + points_from_academy

for point in range(1, number_evaluate_people + 1):
    name_evaluating = input()
    points_from_evaluating = float(input())

    lenght = len(name_evaluating)
    points = (lenght * points_from_evaluating) / 2
    total_points += points



    if total_points > 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!")
        break

if total_points <= 1250.5:
    print(f"Sorry, {name_actor} you need {1250.5 - total_points:.1f} more!")