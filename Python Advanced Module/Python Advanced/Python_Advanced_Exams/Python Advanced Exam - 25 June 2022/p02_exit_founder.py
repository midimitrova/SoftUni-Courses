players = input().split(', ')

players_copy = players.copy()
size = 6
matrix = []
for _ in range(size):
    matrix.append(input().split())

escape_the_maze = False
tom_hits = 0
jerry_hits = 0

while True:

    for player in players:
        first_position = input()
        start_position = []
        for data in first_position:
            if data.isdigit():
                start_position.append(int(data))

        row = start_position[0]
        col = start_position[1]

        if not (0 <= row < size and 0 <= col < size):
            break

        position = matrix[row][col]

        if player == 'Tom' and tom_hits == 1:
            tom_hits += 1
            continue
        elif player == 'Jerry' and jerry_hits == 1:
            jerry_hits += 1
            continue

        if player == 'Tom' and tom_hits > 1:
            tom_hits = 0
        elif player == 'Jerry' and tom_hits > 1:
            jerry_hits = 0

        if position == 'E':
            print(f"{player} found the Exit and wins the game!")
            escape_the_maze = True
            break
        elif position == 'T':
            players_copy.remove(player)
            print(f"{player} is out of the game! The winner is {players_copy[0]}.")
            escape_the_maze = True
            break
        elif position == 'W':
            print(f"{player} hits a wall and needs to rest.")
            if player == 'Tom':
                tom_hits += 1
            else:
                jerry_hits += 1

        players = players_copy

    if escape_the_maze:
        break
