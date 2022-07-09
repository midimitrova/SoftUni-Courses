import sys

number_movies = int(input())

max_rate = - sys.maxsize
min_rate = sys.maxsize
average_rate = 0
total_rate = 0
max_name_movie = ""
min_name_movie = ""

for name in range(1, number_movies + 1):
    name_movie = input()
    rating_movie = float(input())

    if rating_movie > max_rate:
        max_rate = rating_movie
        max_name_movie = name_movie

    if rating_movie < min_rate:
        min_rate = rating_movie
        min_name_movie = name_movie

    total_rate += rating_movie

average_rate = total_rate / number_movies

print(f"{max_name_movie} is with highest rating: {max_rate:.1f}")
print(f"{min_name_movie} is with lowest rating: {min_rate:.1f}")
print(f"Average rating: {average_rate:.1f}")
