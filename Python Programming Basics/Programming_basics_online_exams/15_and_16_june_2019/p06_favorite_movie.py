cnt_movies = 0

total_sum = 0
best_movie = ""
winner_movie = 0


command = input()
while command != "STOP":
    lenght = len(command)

    cnt_movies += 1

    if cnt_movies == 7:
        break

    movie_points = 0
    points = 0

    for ch in command:
        ascii_value = ord(ch)

        if "a" <= ch <= "z":
            points = ascii_value - 2 * lenght
            movie_points += points
        elif "A" <= ch <= "Z":
            points = ascii_value - lenght
            movie_points += points
        else:
            points = ascii_value
            movie_points += ascii_value

    if movie_points > winner_movie:
        winner_movie = movie_points
        best_movie = command
    command = input()
if command == "STOP":
    print(f"The best movie for you is {best_movie} with {winner_movie} ASCII sum.")
elif cnt_movies == 7:
    print("The limit is reached.")
    print(f"The best movie for you is {best_movie} with {winner_movie} ASCII sum.")