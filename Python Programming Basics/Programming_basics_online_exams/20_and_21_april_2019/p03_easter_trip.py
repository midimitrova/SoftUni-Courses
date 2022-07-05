destination = input()
dates = input()
number_nights = int(input())

price_per_night = 0


if dates == "21-23":
    if destination == "France":
        price_per_night = 30
    elif destination == "Italy":
        price_per_night = 28
    elif destination == "Germany":
        price_per_night = 32
elif dates == "24-27":
    if destination == "France":
        price_per_night = 35
    elif destination == "Italy":
        price_per_night = 32
    elif destination == "Germany":
        price_per_night = 37
elif dates == "28-31":
    if destination == "France":
        price_per_night = 40
    elif destination == "Italy":
        price_per_night = 39
    elif destination == "Germany":
        price_per_night = 43

total_price = number_nights * price_per_night

print(f"Easter trip to {destination} : {total_price:.2f} leva.")