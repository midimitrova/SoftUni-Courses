best_player = ""
winner_points = 0
curr_points = 0
total_points = 0
points_cnt = 0
name = input()

while name != "Stop":

    while True:
        lenght = len(name)
        points = input()
        for ch in name:
            points = int(points)
            ascii_value = ord(ch)
            if ascii_value == points:
                curr_points = 10
            elif ascii_value != points:
                curr_points = 2

            total_points += curr_points
            points_cnt += 1

            if lenght == points_cnt:
                break
            points = int(input())

        if total_points >= winner_points:
            winner_points = total_points
            best_player = name

        name = input()

        if name == "Stop":
            print(f"The winner is {best_player} with {winner_points} points!")
            break

        curr_points = 0
        total_points = 0
        points_cnt = 0
