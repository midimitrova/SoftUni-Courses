from math import ceil

number_people = int(input())
entry_price = float(input())
price_chair = float(input())
price_umbrella = float(input())

total_entry = number_people * entry_price
number_umbrella = ceil(number_people / 2)
number_chair = ceil(number_people * 75/100)

total_price = total_entry + number_umbrella * price_umbrella + number_chair * price_chair

print(f"{total_price:.2f} lv.")