days_playing = int(input())

money = 0
win_games = 0
lose_games = 0
day_win = 0
day_lose = 0
total_money = 0

for day in range(1, days_playing + 1):
    sport = input()
    while sport != "Finish":
        result = input()
        if result == "win":
            win_games += 1
            money += 20
        elif result == "lose":
            lose_games += 1
        sport = input()

    if win_games > lose_games:
        money += money * 10/100
        day_win += 1
    else:
        day_lose += 1

    total_money += money

    win_games = 0
    lose_games = 0
    money = 0

if day_win > day_lose:
    total_money += total_money * 20/100
if day_win > day_lose:
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")



