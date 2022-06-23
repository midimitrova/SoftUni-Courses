import math

number_days = int(input())
left_food_kg = int(input())
dog_food_day = float(input())
cat_food_day = float(input())
turtle_food_gr = float(input())

needed_food_dog = number_days * dog_food_day
needed_food_cat = number_days * cat_food_day
needed_food_turtle = number_days * turtle_food_gr / 1000

total_food = needed_food_dog + needed_food_cat + needed_food_turtle

if left_food_kg >= total_food:
    print(f"{math.floor(left_food_kg - total_food)} kilos of food left.")
else:
    print(f"{math.ceil(total_food - left_food_kg)} more kilos of food are needed.")