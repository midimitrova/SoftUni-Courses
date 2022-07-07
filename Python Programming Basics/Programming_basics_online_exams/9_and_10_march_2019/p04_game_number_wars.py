name_first_player = input()
name_second_player = input()

first_player_points = 0
second_player_points = 0
winner = ""
winner_point = 0
command = input()

while command != "End of game":

    card_first = int(command)
    card_second = int(input())

    diff = abs(card_first - card_second)

    if card_first > card_second:
        first_player_points += diff
        winner = name_first_player
        winner_point = first_player_points
    elif card_second > card_first:
        second_player_points += diff
        winner = name_second_player
        winner_point = second_player_points

    if card_first == card_second:
        print("Number wars!")
        command = input()
        card_first = int(command)
        card_second = int(input())
        if card_first > card_second:
            first_player_points += diff
            winner = name_first_player
            winner_point = first_player_points
        else:
            second_player_points += diff
            winner = name_second_player
            winner_point = second_player_points
        print(f"{winner} is winner with {winner_point} points")
        break

    command = input()

if command == "End of game":
    print(f"{name_first_player} has {first_player_points} points")
    print(f"{name_second_player} has {second_player_points} points")




