number_breads = int(input())


winner = ""
winner_points = 0
curr_points = 0

for bread in range(1, number_breads + 1):
    name = input()
    best_baker = False

    while True:

        command = input()

        if command == "Stop":
            break

        points = int(command)
        curr_points += points
        if curr_points > winner_points:
            winner_points = curr_points
            winner = name
            best_baker = True

    print(f"{name} has {curr_points} points.")

    if best_baker:

        print(f"{name} is the new number 1!")



print(f"{winner} won competition with {winner_points} points!")


