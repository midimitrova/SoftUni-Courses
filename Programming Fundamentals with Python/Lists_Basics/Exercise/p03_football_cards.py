team_one = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_two = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

cards_lst = input().split(' ')
cnt_team_one = 11
cnt_team_two = 11
terminated_game = False

for i in range(len(cards_lst)):
    if cards_lst[i] in team_one:
        team_one.remove(cards_lst[i])
        cnt_team_one -= 1
    elif cards_lst[i] in team_two:
        team_two.remove(cards_lst[i])
        cnt_team_two -= 1
    elif cards_lst[i] not in team_one:
        continue
    elif cards_lst[i] not in team_two:
        continue

    if cnt_team_one < 7 or cnt_team_two < 7:
        terminated_game = True
        break

if terminated_game:
    print(f"Team A - {cnt_team_one}; Team B - {cnt_team_two}")
    print("Game was terminated")
else:
    print(f"Team A - {cnt_team_one}; Team B - {cnt_team_two}")
