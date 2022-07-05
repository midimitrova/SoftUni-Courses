from math import ceil

number_guests = int(input())
budget = int(input())

price_kozunak = 4
price_egg = 0.45

number_kozunak = ceil(number_guests / 3)
number_eggs = number_guests * 2

total_price = price_kozunak * number_kozunak + price_egg * number_eggs

if budget >= total_price:
    print(f"Lyubo bought {number_kozunak} Easter bread and {number_eggs} eggs.")
    print(f"He has {budget - total_price:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {total_price - budget:.2f} lv. more.")
