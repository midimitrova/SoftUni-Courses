from collections import deque

size = 7
player_names = deque(input().split(', '))
players_result = {player_names[0]: [501, 0],
                  player_names[1]: [501, 0]}
board = [input().split() for row in range(size)]

while True:
    coordinates = input()
    if not coordinates:
        break
    row, col = tuple(map(int, coordinates[1:-1].split(', ')))
    current_player = player_names.popleft()
    players_result[current_player][1] += 1
    if 0 <= row < size and 0 <= col < size:
        symbol = board[row][col]
        hit = 0
        if symbol == 'D':
            points_col = 0
            points_row = 0
            for x in board[row]:
                if x.isdigit():
                    points_row += int(x)
            for x in board:
                if x[col].isdigit():
                    points_col += int(x[col])
            sum_points = 2 * (points_col + points_row)
            hit = sum_points
        elif symbol == 'T':
            points_col = 0
            points_row = 0
            for x in board[row]:
                if x.isdigit():
                    points_row += int(x)
            for x in board:
                if x[col].isdigit():
                    points_col += int(x[col])
            sum_points = 3 * (points_col + points_row)
            hit = sum_points
        elif symbol == 'B':
            players_result[current_player][0] = 0
            break
        else:
            hit = int(symbol)
        players_result[current_player][0] -= hit
        if players_result[current_player][0] <=0:
            break
    player_names.append(current_player)

game_result = dict(sorted(players_result.items(), key=lambda x: (x[1][0])))
winner = list(game_result.keys())[0]
turns = game_result[winner][1]
print(f'{winner} won the game with {turns} throws!')