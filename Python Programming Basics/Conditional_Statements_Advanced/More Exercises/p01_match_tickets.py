budget = float(input())
category = input()
number_people = int(input())


vip_tickets = 499.99
normal_tickets = 249.99

price_VIP_tickets = number_people * vip_tickets
price_normal_tickets = number_people * normal_tickets

transport_expense = 0


if 1 <= number_people <= 4:
    transport_expense = budget * 75/100
elif 5 <= number_people <= 9:
    transport_expense = budget * 60/100
elif 10 <= number_people <= 24:
    transport_expense = budget * 50/100
elif 25 <= number_people <= 49:
    transport_expense = budget * 40/100
elif number_people >= 50:
    transport_expense = budget * 25/100

left_money = budget - transport_expense

if category == "VIP":
    if left_money >= price_VIP_tickets:
        print(f"Yes! You have {left_money - price_VIP_tickets:.2f} leva left.")
    else:
        print(f"Not enough money! You need {price_VIP_tickets - left_money:.2f} leva.")
elif category == "Normal":
    if left_money >= price_normal_tickets:
        print(f"Yes! You have {left_money - price_normal_tickets:.2f} leva left.")
    else:
        print(f"Not enough money! You need {price_normal_tickets - left_money:.2f} leva.")