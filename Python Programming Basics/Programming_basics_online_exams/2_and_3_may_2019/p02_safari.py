budget = float(input())
littre_fuel_needed = float(input())
day = input()

price_fuel = littre_fuel_needed * 2.10
guide = 100
total_price = price_fuel + guide

if day == "Saturday":
    discount = total_price * 10/100
    total_price -= discount
elif day == "Sunday":
    discount = total_price * 20/100
    total_price -= discount

if budget > total_price:
    print(f"Safari time! Money left: {budget - total_price:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {total_price - budget:.2f} lv.")
