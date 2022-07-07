from math import floor

number_games = int(input())
enter_points = int(input())

points = 0
total_points = 0
win_game = 0

for game in range(1, number_games + 1):
    stage_of_game = input()

    if stage_of_game == "W":
        points = 2000
        total_points += points
        win_game += 1
    elif stage_of_game == "F":
        points = 1200
        total_points += points
    elif stage_of_game == "SF":
        points = 720
        total_points += points

total_points += enter_points
average_points = ((total_points - enter_points) / number_games)

if win_game > 0:
    win_game = (win_game / number_games) * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{win_game:.2f}%")