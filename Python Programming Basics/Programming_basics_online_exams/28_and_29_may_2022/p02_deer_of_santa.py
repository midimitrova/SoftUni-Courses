from math import floor, ceil

number_days = int(input())
left_food_kg = int(input())
first_deer_food_for_day = float(input())
second_deer_food_for_day = float(input())
third_deer_food_for_day = float(input())


total_food = number_days * first_deer_food_for_day + number_days * second_deer_food_for_day + \
             number_days * third_deer_food_for_day

if left_food_kg >= total_food:
    print(f"{floor(left_food_kg - total_food)} kilos of food left.")
else:
    print(f"{ceil(total_food - left_food_kg)} more kilos of food are needed.")