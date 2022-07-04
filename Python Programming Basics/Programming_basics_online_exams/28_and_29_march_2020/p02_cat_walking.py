minutes_walking_day = int(input())
number_walkings_day = int(input())
calories_day = int(input())

total_minutes_walking = number_walkings_day * minutes_walking_day
burned_calories = total_minutes_walking * 5
half_of_calories = calories_day * 50/100

if burned_calories >= half_of_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")