from math import floor

number_balls = int(input())

red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_colour_balls = 0
total_points = 0


for colour in range(1, number_balls + 1):
    colour_balls = input()

    if colour_balls == "red":
        red_balls += 1
        total_points += 5
    elif colour_balls == "orange":
        orange_balls += 1
        total_points += 10
    elif colour_balls == "yellow":
        yellow_balls += 1
        total_points += 15
    elif colour_balls == "white":
        white_balls += 1
        total_points += 20
    elif colour_balls == "black":
        black_balls += 1
        total_points = total_points / 2
    else:
        other_colour_balls += 1
        total_points

print(f"Total points: {floor(total_points)}")
print(f"Red balls: {floor(red_balls)}")
print(f"Orange balls: {floor(orange_balls)}")
print(f"Yellow balls: {floor(yellow_balls)}")
print(f"White balls: {floor(white_balls)}")
print(f"Other colors picked: {floor(other_colour_balls)}")
print(f"Divides from black balls: {floor(black_balls)}")


