from math import ceil

time_photos = int(input())
number_scenes = int(input())
time_scene = int(input())

preparation_time = time_photos * 15/100
total_time = preparation_time + number_scenes * time_scene

if time_photos >= total_time:
    print(f"You managed to finish the movie on time! You have {ceil(time_photos - total_time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {ceil(total_time - time_photos)} minutes.")