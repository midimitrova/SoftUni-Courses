excursion_price = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

price_for_puzzles = number_of_puzzles * 2.60
price_for_dolls = number_of_dolls * 3
price_for_bears = number_of_bears * 4.10
price_for_minions = number_of_minions * 8.20
price_for_trucks = number_of_trucks * 2

total_number_of_toys = number_of_trucks + number_of_minions + number_of_bears + number_of_dolls + number_of_puzzles

total_price = price_for_puzzles + price_for_dolls + price_for_bears + price_for_minions + price_for_trucks

if total_number_of_toys >= 50:
    discount = total_price * 0.25
    total_price = total_price - discount

rent_price = total_price * 0.1

final_sum = total_price - rent_price

if final_sum >= excursion_price:
   print(f"Yes! {final_sum - excursion_price:.2f} lv left.")
else:
    print(f"Not enough money! {excursion_price - final_sum:.2f} lv needed.")