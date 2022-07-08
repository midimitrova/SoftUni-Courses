budget = float(input())
number_nights = int(input())
price_night = float(input())
percentage_more_expense = int(input())

if number_nights > 7:
    discount = price_night * 5/100
    price_night -= discount

price_all_nights = number_nights * price_night

price_more_expense = budget * percentage_more_expense / 100

total_price = price_all_nights + price_more_expense

if budget >= total_price:
    print(f"Ivanovi will be left with {budget - total_price:.2f} leva after vacation.")
else:
    print(f"{total_price - budget:.2f} leva needed.")