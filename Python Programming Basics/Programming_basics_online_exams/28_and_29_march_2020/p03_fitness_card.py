budget = float(input())
gender = input()
age = int(input())
type_sport = input()

price_per_month = 0

if type_sport == "Gym":
    if gender == "m":
        price_per_month = 42
    elif gender == "f":
        price_per_month = 35
elif type_sport == "Boxing":
    if gender == "m":
        price_per_month = 41
    elif gender == "f":
        price_per_month = 37
elif type_sport == "Yoga":
    if gender == "m":
        price_per_month = 45
    elif gender == "f":
        price_per_month = 42
elif type_sport == "Zumba":
    if gender == "m":
        price_per_month = 34
    elif gender == "f":
        price_per_month = 31
elif type_sport == "Dances":
    if gender == "m":
        price_per_month = 51
    elif gender == "f":
        price_per_month = 53
elif type_sport == "Pilates":
    if gender == "m":
        price_per_month = 39
    elif gender == "f":
        price_per_month = 37

if age <= 19:
    price_per_month -= price_per_month * 20/100

if budget >= price_per_month:
    print(f"You purchased a 1 month pass for {type_sport}.")
else:
    print(f"You don't have enough money! You need ${price_per_month - budget:.2f} more.")