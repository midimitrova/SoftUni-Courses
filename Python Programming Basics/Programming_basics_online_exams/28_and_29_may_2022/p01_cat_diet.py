percentage_fat = int(input()) / 100
percentage_proteins = int(input()) /100
percentage_carbohydrates = int(input()) / 100
total_calories = int(input())
percentage_water = int(input())

fat_day_for_gr = (percentage_fat * total_calories) / 9
proteins_day_for_gr = (percentage_proteins * total_calories) / 4
carbohydrates_day_for_gr = (percentage_carbohydrates * total_calories) / 4

total_food = fat_day_for_gr + proteins_day_for_gr + carbohydrates_day_for_gr
calories_for_gr = total_calories / total_food
percentage_calories = 100 - percentage_water
calories = (percentage_calories * calories_for_gr)  / 100
print(f"{calories:.4f}")
