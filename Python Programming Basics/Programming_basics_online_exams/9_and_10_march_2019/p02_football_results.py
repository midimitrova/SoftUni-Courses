first_game = input()
second_game = input()
third_game = input()


win_games = 0
lose_games = 0
draw_games = 0


if first_game[0] > first_game[2]:
    win_games += 1
elif first_game[0] < first_game[2]:
    lose_games += 1
elif first_game[0] == first_game[2]:
    draw_games += 1

if ord(second_game[0]) > ord(second_game[2]):
    win_games += 1
elif ord(second_game[0]) < ord(second_game[2]):
    lose_games += 1
elif ord(second_game[0]) == ord(second_game[2]):
    draw_games +=1

if ord(third_game[0]) > ord(third_game[2]):
    win_games += 1
elif ord(third_game[0]) < ord(third_game[2]):
    lose_games += 1
elif ord(third_game[0]) == ord(third_game[2]):
    draw_games += 1

print(f"Team won {win_games} games.")
print(f"Team lost {lose_games} games.")
print(f"Drawn games: {draw_games}")
