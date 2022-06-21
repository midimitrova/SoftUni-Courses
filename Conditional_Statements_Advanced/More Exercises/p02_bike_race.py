number_juniors = int(input())
number_seniors = int(input())
type_trace = input()

total_people = number_juniors + number_seniors

if type_trace == "trail":
    price_juniors = number_juniors * 5.50
    price_seniors = number_seniors * 7
    total_price = price_juniors + price_seniors
elif type_trace == "cross-country":
    price_juniors = number_juniors * 8
    price_seniors = number_seniors * 9.50
    total_price = price_juniors + price_seniors
    if total_people >= 50:
        total_price = price_juniors + price_seniors
        total_price -= total_price * 25/100
elif type_trace == "downhill":
    price_juniors = number_juniors * 12.25
    price_seniors = number_seniors * 13.75
    total_price = price_juniors + price_seniors
elif type_trace == "road":
    price_juniors = number_juniors * 20
    price_seniors = number_seniors * 21.50
    total_price = price_juniors + price_seniors

total_price_without_tax = total_price - total_price * 5/100
print(f"{total_price_without_tax:.2f}")

