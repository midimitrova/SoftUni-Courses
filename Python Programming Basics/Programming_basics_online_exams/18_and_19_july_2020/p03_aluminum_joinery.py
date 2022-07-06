number_joinery = int(input())
type_joinery = input()
type_delivery = input()

price = 0
discount = 0
price_delivery = 60

if type_joinery == "90X130":
    price = 110
    if number_joinery > 60:
        discount = 0.08
    elif number_joinery > 30:
        discount = 0.05
    else:
        price
elif type_joinery == "100X150":
    price = 140
    if number_joinery > 80:
        discount = 0.1
    elif number_joinery > 40:
        discount = 0.06
    else:
        price
elif type_joinery == "130X180":
    price = 190
    if number_joinery > 50:
        discount = 0.12
    elif number_joinery > 20:
        discount = 0.07
    else:
        price
elif type_joinery == "200X300":
    price = 250
    if number_joinery > 50:
        discount = 0.14
    elif number_joinery > 25:
        discount = 0.09
    else:
        price

total_price = (price - price * discount) * number_joinery


if type_delivery == "With delivery":
    total_price += price_delivery
else:
    total_price

if number_joinery > 99:
    total_price -= total_price * 4/100


if number_joinery < 10:
    print("Invalid order")
else:
    print(f"{total_price:.2f} BGN")


