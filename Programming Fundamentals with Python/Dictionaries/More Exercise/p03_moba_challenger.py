players = {}
players_skills = {}

command = input()

while '->' in command:

    if command == 'Season end':
        break

    player_name, position, skill = command.split(' -> ')
    skill = int(skill)
    if player_name not in players_skills.keys():
        players_skills[player_name] = skill

    if player_name not in players.keys():
        players[player_name] = {position: skill}
    else:
        if position in players[player_name].keys():
            if players[player_name][position] < skill:
                players_skills[player_name] -= players[player_name][position]
                players[player_name][position] = skill
                players_skills[player_name] += skill

        else:
            players[player_name][position] = skill
            players_skills[player_name] += skill

    command = input()

while command != 'Season end':
    player_one, player_two = command.split(' vs ')

    if (player_one and player_two) in players.keys():
        for position_one in players[player_one].keys():
            if position_one in players[player_two].keys():
                if players_skills[player_one] > players_skills[player_two]:
                    del players[player_two]
                    del players_skills[player_two]
                elif players_skills[player_one] < players_skills[player_two]:
                    del players[player_one]
                    del players_skills[player_one]
                break

    command = input()

sorted_skill = sorted(players_skills.items(), key=lambda item: (-item[1], item[0]))

for name, skill in sorted_skill:
    print(f"{name}: {skill} skill")

    for name_player, positions in players.items():
        if name == name_player:
            sorted_players = sorted(positions.items(), key=lambda item: (-item[1], item[0]))
            for position in sorted_players:
                print(f'- {position[0]} <::> {position[1]}')
