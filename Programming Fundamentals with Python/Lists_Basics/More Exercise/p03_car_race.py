sequence_of_numbers = input().split()

number_to_int = []
winner = ''

for number in sequence_of_numbers:
    number_to_int.append(int(number))

middle_of_numbers = len(number_to_int) // 2
first_car_left = number_to_int[0:middle_of_numbers]
second_car_right = number_to_int[middle_of_numbers + 1:][::-1]

total_time_first = 0
for time_first in first_car_left:
    total_time_first += time_first
    if time_first == 0:
        total_time_first *= 0.8

total_time_second = 0
for time_second in second_car_right:
    total_time_second += time_second
    if time_second == 0:
        total_time_second *= 0.8

if total_time_first < total_time_second:
    winner = 'left'
    print(f"The winner is {winner} with total time: {total_time_first:.1f}")
elif total_time_first >= total_time_second:
    winner = 'right'
    print(f"The winner is {winner} with total time: {total_time_second:.1f}")
