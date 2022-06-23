number_chrysanthemum = int(input())
number_rose = int(input())
number_tulip = int(input())
season = input()
holiday_or_not = input()

price_chrysanthemum = 0
price_rose = 0
price_tulip = 0
total_price = price_chrysanthemum + price_rose + price_tulip
total_number = number_chrysanthemum + number_rose + number_tulip

if season == "Spring" or season == "Summer":
    price_chrysanthemum = number_chrysanthemum * 2
    price_rose = number_rose * 4.10
    price_tulip = number_tulip * 2.50
    total_price = price_chrysanthemum + price_rose + price_tulip

    if holiday_or_not == "Y":
        total_price += total_price * 15/100
    else:
        total_price
    if number_tulip > 7 and season == "Spring":
        total_price -= total_price * 5/100
    else:
        total_price
elif season == "Autumn" or season == "Winter":
    price_chrysanthemum = number_chrysanthemum * 3.75
    price_rose = number_rose * 4.50
    price_tulip = number_tulip * 4.15
    total_price = price_chrysanthemum + price_rose + price_tulip
    if holiday_or_not == "Y":
        total_price += total_price * 15/100
    else:
        total_price
    if number_rose >= 10 and season == "Winter":
        total_price -= total_price * 10/100
    else:
        total_price

if total_number > 20:
    total_price -= total_price * 20/100

print(f"{2 + total_price:.2f}")