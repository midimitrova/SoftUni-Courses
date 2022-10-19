quantity_food_in_kilograms = float(input())
quantity_hay_in_kilograms = float(input())
quantity_cover_in_kilograms = float(input())
weight_in_kilograms = float(input())
is_enough = False

while True:
    quantity_food_in_grams = quantity_food_in_kilograms * 1000
    quantity_hay_in_grams = quantity_hay_in_kilograms * 1000
    quantity_cover_in_grams = quantity_cover_in_kilograms * 1000
    weight_in_grams = weight_in_kilograms * 1000

    for day in range(1, 31):
        quantity_food_in_grams -= 300

        if day % 2 == 0:
            hay_per_day = quantity_food_in_grams * 5/100
            quantity_hay_in_grams -= hay_per_day
        if day % 3 == 0:
            cover_per_day = weight_in_grams * 1/3
            quantity_cover_in_grams -= cover_per_day

    if quantity_food_in_grams <= 0 or quantity_cover_in_grams <= 0 or quantity_hay_in_grams <= 0:
        break
    else:
        is_enough = True
        break

if is_enough:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food_in_grams/1000:.2f}, Hay: {quantity_hay_in_grams/1000:.2f}, Cover: {quantity_cover_in_grams/1000:.2f}.")
else:
    print("Merry must go to the pet store!")

