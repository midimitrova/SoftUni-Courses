days = int(input())
type_room = input()
grade = input()

nights = days - 1
price = 0

if nights < 10:
    if type_room == "room for one person":
        price = nights * 18
    elif type_room == "apartment":
        price = nights * 25
        price -= price * 30/100
    elif type_room == "president apartment":
        price = nights * 35
        price -= price * 10/100
elif 10 <= nights <= 15:
    if type_room == "room for one person":
        price = nights * 18
    elif type_room == "apartment":
        price = nights * 25
        price -= price * 35 / 100
    elif type_room == "president apartment":
        price = nights * 35
        price -= price * 15/100
elif nights > 15:
    if type_room == "room for one person":
        price = nights * 18
    elif type_room == "apartment":
        price = nights * 25
        price -= price * 50/100
    elif type_room == "president apartment":
        price = nights * 35
        price -= price * 20/100

if grade == "positive":
    price += price * 25/100
elif grade == "negative":
    price -= price * 10/100

print(f"{price:.2f}")