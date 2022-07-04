bought_food = int(input())
bought_food_in_gram = bought_food * 1000
total_quantity = 0

command = input()

while True:
    if command == "Adopted":
        break

    food = int(command)
    total_quantity += food

    command = input()


if total_quantity <= bought_food_in_gram:
    print(f"Food is enough! Leftovers: {bought_food_in_gram - total_quantity} grams.")
else:
    print(f"Food is not enough. You need {total_quantity - bought_food_in_gram} grams more.")