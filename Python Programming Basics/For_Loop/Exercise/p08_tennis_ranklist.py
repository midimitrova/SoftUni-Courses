from math import floor

number_tournament = int(input())
enter_points = int(input())

points = 0
total_points = 0 + enter_points
number_games = 0
percentage = 0


for tour in range(1, number_tournament + 1):
    stage_of_tournament = input()

    if stage_of_tournament == "W":
        points = 2000
        number_games += 1
        percentage += 1

    elif stage_of_tournament == "F":
        points = 1200
        number_games += 1
    elif stage_of_tournament == "SF":
        points = 720
        number_games += 1

    total_points += points



if percentage > 0:
        percentage = (percentage / number_games) * 100

average_win_games = (total_points - enter_points) / number_games

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_win_games)}")
print(f"{percentage:.2f}%")
