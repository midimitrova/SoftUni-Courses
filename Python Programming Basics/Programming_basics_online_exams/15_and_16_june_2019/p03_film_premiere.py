projection = input()
package_for_film = input()
number_tickets = int(input())

price_ticket = 0
discount = 0

if projection == "John Wick":
    if package_for_film == "Drink":
        price_ticket = 12
    elif package_for_film == "Popcorn":
        price_ticket = 15
    elif package_for_film == "Menu":
        price_ticket = 19
elif projection == "Star Wars":
    if package_for_film == "Drink":
        price_ticket = 18
    elif package_for_film == "Popcorn":
        price_ticket = 25
    elif package_for_film == "Menu":
        price_ticket = 30
elif projection == "Jumanji":
    if package_for_film == "Drink":
        price_ticket = 9
    elif package_for_film == "Popcorn":
        price_ticket = 11
    elif package_for_film == "Menu":
        price_ticket = 14

total_price = number_tickets * price_ticket

if projection == "Star Wars" and number_tickets >= 4:
    discount = 0.3
    total_price -= total_price * discount

if projection == "Jumanji" and number_tickets == 2:
    discount = 0.15
    total_price -= total_price * discount

print(f"Your bill is {total_price:.2f} leva.")

