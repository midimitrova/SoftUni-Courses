name = input()
number_days = int(input())
number_tickets = int(input())
price_ticket = float(input())
percentage_cinema = int(input())

price_ticket_day = number_tickets * price_ticket
price_for_period = price_ticket_day * number_days
money_for_cinema = price_for_period * percentage_cinema / 100
income = price_for_period - money_for_cinema

print(f"The profit from the movie {name} is {income:.2f} lv.")