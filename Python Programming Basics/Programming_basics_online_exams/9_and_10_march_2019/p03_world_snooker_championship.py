stage_of_championship = input()
type_ticket = input()
number_tickets = int(input())
photo = input()

price = 0
discount = 0

if stage_of_championship == "Quarter final":
    if type_ticket == "Standard":
        price = 55.50
    elif type_ticket == "Premium":
        price = 105.20
    elif type_ticket == "VIP":
        price = 118.90
elif stage_of_championship == "Semi final":
    if type_ticket == "Standard":
        price = 75.88
    elif type_ticket == "Premium":
        price = 125.22
    elif type_ticket == "VIP":
        price = 300.40
elif stage_of_championship == "Final":
    if type_ticket == "Standard":
        price = 110.10
    elif type_ticket == "Premium":
        price = 160.66
    elif type_ticket == "VIP":
        price = 400

total_price = price * number_tickets

if total_price > 4000:
    discount = 0.25
    total_price -= total_price * discount
    if photo == "Y":
        total_price
elif total_price > 2500:
    discount = 0.1
    total_price -= total_price * discount
    if photo == "Y":
        total_price += 40 * number_tickets
    else:
        total_price
elif total_price <= 2500:
    if photo == "Y":
        total_price += 40 * number_tickets
    else:
        total_price

print(f"{total_price:.2f}")