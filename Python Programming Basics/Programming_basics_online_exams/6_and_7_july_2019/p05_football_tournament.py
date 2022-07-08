name_team = input()
number_games = int(input())

points = 0
total_points = 0
win_games = 0
draw_games = 0
lost_games = 0

for _ in range(1, number_games + 1):
    result = input()

    if result == "W":
        points = 3
        total_points += points
        win_games += 1
    elif result == "D":
        points = 1
        total_points += points
        draw_games += 1
    elif result == "L":
        points = 0
        total_points += points
        lost_games += 1

if number_games == 0:
    print(f"{name_team} hasn't played any games during this season.")
elif number_games > 0:
    print(f"{name_team} has won {total_points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {win_games}")
    print(f"## D: {draw_games}")
    print(f"## L: {lost_games}")
    print(f"Win rate: {(win_games / number_games) * 100:.2f}%")