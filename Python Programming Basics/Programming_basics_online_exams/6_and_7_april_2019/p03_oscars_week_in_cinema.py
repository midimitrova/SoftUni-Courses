name_film = input()
type_room = input()
number_tickets = int(input())

price_per_ticket = 0

if name_film == "A Star Is Born":
    if type_room == "normal":
        price_per_ticket = 7.50
    elif type_room == "luxury":
        price_per_ticket = 10.50
    elif type_room == "ultra luxury":
        price_per_ticket = 13.50
elif name_film == "Bohemian Rhapsody":
    if type_room == "normal":
        price_per_ticket = 7.35
    elif type_room == "luxury":
        price_per_ticket = 9.45
    elif type_room == "ultra luxury":
        price_per_ticket = 12.75
elif name_film == "Green Book":
    if type_room == "normal":
        price_per_ticket = 8.15
    elif type_room == "luxury":
        price_per_ticket = 10.25
    elif type_room == "ultra luxury":
        price_per_ticket = 13.25
elif name_film == "The Favourite":
    if type_room == "normal":
        price_per_ticket = 8.75
    elif type_room == "luxury":
        price_per_ticket = 11.55
    elif type_room == "ultra luxury":
        price_per_ticket = 13.95

total_price = price_per_ticket * number_tickets

print(f"{name_film} -> {total_price:.2f} lv.")