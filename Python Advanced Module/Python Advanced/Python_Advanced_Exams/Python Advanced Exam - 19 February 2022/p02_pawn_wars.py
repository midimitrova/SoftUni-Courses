size = 8
player_location = {'w': [], 'b': []}
figure_color = {'w': 'White', 'b': 'Black'}

first_letter_ascii = 97
chess_board = []
directions_dict = {'l': (0, -1), 'r': (0, 1)}
for row in range(size):
    line = input().split()
    if 'w' in line:
        player_location['w'] = [row, line.index('w')]
    if 'b' in line:
        player_location['b'] = [row, line.index('b')]
    chess_board.append(line)

winner = False
square = ''
while not winner:

    for pawn in player_location:
        operator = '-' if pawn == 'w' else '+'
        for way in directions_dict.values():
            try_row, try_col = eval(str(player_location[pawn][0]) + operator + '1'), way[1] + player_location[pawn][1]
            if 0 <= try_row < size and 0 <= try_col < size:
                if chess_board[try_row][try_col] != '-':
                    square = chr(first_letter_ascii + try_col) + str(size - try_row)
                    winner = True
                    break
        if winner:
            print(f"Game over! {figure_color[pawn]} win, capture on {square}.")
            break
        chess_board[player_location[pawn][0]][player_location[pawn][1]] = '-'

        pawn_row = eval(str(player_location[pawn][0]) + operator + '1')
        pawn_col = player_location[pawn][1]
        player_location[pawn] = [pawn_row, pawn_col]
        chess_board[pawn_row][pawn_col] = pawn
        if pawn_row == 0 or pawn_row == size - 1:
            square = chr(first_letter_ascii + pawn_col) + str(size - pawn_row)
            print(f"Game over! {figure_color[pawn]} pawn is promoted to a queen at {square}.")
            winner = True
            break