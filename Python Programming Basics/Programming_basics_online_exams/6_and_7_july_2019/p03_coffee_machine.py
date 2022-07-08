drink = input()
type_sugar = input()
number_drinks = int(input())

price = 0
discount = 0

if drink == "Espresso":
    if type_sugar == "Without":
        price = 0.90
    elif type_sugar == "Normal":
        price = 1
    elif type_sugar == "Extra":
        price = 1.20
elif drink == "Cappuccino":
    if type_sugar == "Without":
        price = 1
    elif type_sugar == "Normal":
        price = 1.20
    elif type_sugar == "Extra":
        price = 1.60
elif drink == "Tea":
    if type_sugar == "Without":
        price = 0.50
    elif type_sugar == "Normal":
        price = 0.60
    elif type_sugar == "Extra":
        price = 0.70

total_price = price * number_drinks

if type_sugar == "Without":
    discount = 0.35
    total_price -= total_price * discount
if drink == "Espresso" and number_drinks >= 5:
    discount = 0.25
    total_price -= total_price * discount
if total_price > 15:
    discount = 0.2
    total_price -= total_price * discount

print(f"You bought {number_drinks} cups of {drink} for {total_price:.2f} lv.")

