import math
from math import ceil

name_serial = input()
time_one_episode = int(input())
time_for_break = int(input())

time_for_lunch = time_for_break * 1/8
time_for_rest = time_for_break * 1/4

total_time = time_for_lunch + time_for_rest + time_one_episode

if total_time <= time_for_break:
    print(f"You have enough time to watch {name_serial} and left with {math.ceil(time_for_break - total_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_serial}, you need {math.ceil(total_time - time_for_break)} more minutes.")