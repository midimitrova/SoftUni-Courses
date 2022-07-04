number_days = int(input())
total_food = float(input())

total_food_day = 0
biscuits = 0
food_dog_eaten = 0
food_cat_eaten = 0

for day in range(1, number_days + 1):
    food_dog = int(input())
    food_cat = int(input())

    food_day = food_dog + food_cat
    total_food_day += food_day
    food_dog_eaten += food_dog
    food_cat_eaten += food_cat

    if day % 3 == 0:
        current_biscuits = food_day * 10/100
        biscuits += current_biscuits

percentage_total_food = (total_food_day / total_food) * 100
percentage_dog_food = (food_dog_eaten / total_food_day) * 100
percentage_cat_food = (food_cat_eaten / total_food_day) * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{percentage_total_food:.2f}% of the food has been eaten.")
print(f"{percentage_dog_food:.2f}% eaten from the dog.")
print(f"{percentage_cat_food:.2f}% eaten from the cat.")


