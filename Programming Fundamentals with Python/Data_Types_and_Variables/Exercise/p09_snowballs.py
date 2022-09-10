number_of_snowballs = int(input())

max_snowball_value = 0
max_weight = 0
max_time = 0
max_quality = 0

while number_of_snowballs > 0:

    weight_of_the_snowball = int(input())
    time_needed = int(input())
    quality = int(input())

    snowball_value = round((weight_of_the_snowball / time_needed) ** quality)

    if snowball_value > max_snowball_value:
        max_snowball_value = snowball_value
        max_weight = weight_of_the_snowball
        max_time = time_needed
        max_quality = quality


    number_of_snowballs -= 1

print(f"{max_weight} : {max_time} = {max_snowball_value} ({max_quality})")