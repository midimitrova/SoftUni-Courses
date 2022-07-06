name = input()
number_tickets_adult = int(input())
number_tickets_child = int(input())
net_price_adult = float(input())
tax = float(input())

net_price_child = net_price_adult - net_price_adult * 70/100
price_tax = (number_tickets_child + number_tickets_adult)
total_price = number_tickets_adult * net_price_adult + number_tickets_child * net_price_child + tax * price_tax
final = total_price * 20/100

print(f"The profit of your agency from {name} tickets is {final:.2f} lv.")
