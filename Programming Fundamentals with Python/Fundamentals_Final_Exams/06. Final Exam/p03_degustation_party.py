meals_data = {}

dislike_counter = 0
while True:

    data = input().split('-')

    if data[0] == 'Stop':
        break
    elif data[0] == 'Like':
        guest = data[1]
        meal = data[2]
        if guest not in meals_data:
            meals_data[guest] = [meal]
        else:
            if meal not in meals_data[guest]:
                meals_data[guest].append(meal)
    elif data[0] == 'Dislike':
        guest = data[1]
        meal = data[2]
        if guest not in meals_data.keys():
            print(f"{guest} is not at the party.")
        elif meal not in meals_data[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        elif meal in meals_data[guest]:
            print(f"{guest} doesn't like the {meal}.")
            dislike_counter += 1
            meals_data[guest].remove(meal)

for guest, meals in meals_data.items():
    print(f"{guest}: {', '.join(meals)}")
print(f'Unliked meals: {dislike_counter}')

