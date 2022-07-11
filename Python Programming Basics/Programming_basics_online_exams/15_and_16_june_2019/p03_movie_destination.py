budget = float(input())
destination = input()
season = input()
number_days = int(input())

price_per_day = 0
discount = 0
increase_in_price = 0

if destination == "Dubai":
    if season == "Winter":
        price_per_day = 45000
    elif season == "Summer":
        price_per_day = 40000
elif destination == "Sofia":
    if season == "Winter":
        price_per_day = 17000
    elif season == "Summer":
        price_per_day = 12500
elif destination == "London":
    if season == "Winter":
        price_per_day = 24000
    elif season == "Summer":
        price_per_day = 20250

total_price = price_per_day * number_days

if destination == "Dubai":
    discount = 0.3
    total_price -= total_price * discount
elif destination == "Sofia":
    increase_in_price = 0.25
    total_price += total_price * increase_in_price

if budget >= total_price:
    print(f"The budget for the movie is enough! We have {budget - total_price:.2f} leva left!")
else:
    print(f"The director needs {total_price - budget:.2f} leva more!")