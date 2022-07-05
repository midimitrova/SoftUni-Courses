eggs_first_player = int(input())
eggs_second_player = int(input())

winner = ''


while winner != "End":
    winner = input()

    if winner == "two":
        eggs_first_player -= 1
        if eggs_first_player == 0:
            print(f"Player one is out of eggs. Player two has {eggs_second_player} eggs left.")
            break
    elif winner == "one":
        eggs_second_player -= 1
        if eggs_second_player == 0:
            print(f"Player two is out of eggs. Player one has {eggs_first_player} eggs left.")
            break

if winner == "End":
    print(f"Player one has {eggs_first_player} eggs left.")
    print(f"Player two has {eggs_second_player} eggs left.")





















