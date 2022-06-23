budget = int(input())
season = input()
number_fishman = int(input())

rent_ship = 0

if season == "Spring":
    rent_ship = 3000
    if number_fishman <= 6:
        price = rent_ship - rent_ship * 10 / 100
        if number_fishman % 2 == 0:
            price = price - price * 5 / 100
    elif 7 < number_fishman <= 11:
        price = rent_ship - rent_ship * 15 / 100
        if number_fishman % 2 == 0:
            price = price - price * 5 / 100
    elif number_fishman > 12:
        price = rent_ship - rent_ship * 25 / 100
        if number_fishman % 2 == 0:
            price = price - price * 5 / 100

elif season == "Summer":
    rent_ship = 4200
    if number_fishman <= 6:
        price = rent_ship - rent_ship * 10/100
        if number_fishman % 2 == 0:
            price = price - price * 5 / 100
    elif 7 < number_fishman <= 11:
        price = rent_ship - rent_ship * 15/100
        if number_fishman % 2 == 0:
            price = price - price * 5 / 100
    elif number_fishman > 12:
        price = rent_ship - rent_ship * 25/100
        if number_fishman % 2 == 0:
            price = price - price * 5 / 100

elif season == "Autumn":
    rent_ship = 4200
    if number_fishman <= 6:
        price = rent_ship - rent_ship * 10 / 100
    elif 7 < number_fishman <= 11:
        price = rent_ship - rent_ship * 15 / 100
    elif number_fishman > 12:
        price = rent_ship - rent_ship * 25 / 100


elif season == "Winter":
    rent_ship = 2600
    if number_fishman <= 6:
        price = rent_ship - rent_ship * 10 / 100
        if number_fishman % 2 == 0:
            price = price - price * 5 / 100
    elif 7 < number_fishman <= 11:
        price = rent_ship - rent_ship * 15 / 100
        if number_fishman % 2 == 0:
            price = price - price * 5 / 100
    elif number_fishman > 12:
        price = rent_ship - rent_ship * 25 / 100
        if number_fishman % 2 == 0:
            price = price - price * 5 / 100

if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")



