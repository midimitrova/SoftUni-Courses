from math import floor

name = input()
number_seasons = int(input())
number_episode = int(input())
episode_min_without_advertising = float(input())

time_advertising = episode_min_without_advertising * 20/100
time_episode_with_adv = time_advertising + episode_min_without_advertising
special_episode = number_seasons * 10

total_time = time_episode_with_adv * number_episode * number_seasons + special_episode

print(f"Total time needed to watch the {name} series is {floor(total_time)} minutes.")