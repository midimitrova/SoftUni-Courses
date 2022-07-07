
win_games_cnt = 0
lost_games_cnt = 0
games_cnt = 0

name_tour = input()


while name_tour != "End of tournaments":
    number_games = int(input())
    for game in range(1, number_games + 1):

        points_our_team = int(input())
        points_other_team = int(input())
        games_cnt += 1
        if points_our_team > points_other_team:
            diff = points_our_team - points_other_team
            win_games_cnt += 1

            print(f"Game {games_cnt} of tournament "
                  f"{name_tour}: win with {diff} points.")

        if points_our_team < points_other_team:
            diff = points_other_team- points_our_team
            lost_games_cnt += 1
            # is_win_game = False
            print(f"Game {games_cnt} of tournament {name_tour}: "
                  f"lost with {diff} points.")

    games_cnt = 0
    name_tour = input()
    # number_games = int(input())

if name_tour == "End of tournaments":
    print(f"{(win_games_cnt / (win_games_cnt + lost_games_cnt)) * 100:.2f}% matches win")
    print(f"{(lost_games_cnt / (win_games_cnt + lost_games_cnt)) * 100:.2f}% matches lost")



