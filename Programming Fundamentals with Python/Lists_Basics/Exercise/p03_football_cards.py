team_one = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_two = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

cards_lst = input().split(' ')
terminated_game = False

for i in range(len(cards_lst)):
    if cards_lst[i] in team_one:
        team_one.remove(cards_lst[i])
    elif cards_lst[i] in team_two:
        team_two.remove(cards_lst[i])
    elif cards_lst[i] not in team_one:
        continue
    elif cards_lst[i] not in team_two:
        continue

    if len(team_one) < 7 or len(team_two) < 7:
        terminated_game = True
        break
print(f"Team A - {len(team_one)}; Team B - {len(team_two)}")
if terminated_game:
    print("Game was terminated")

