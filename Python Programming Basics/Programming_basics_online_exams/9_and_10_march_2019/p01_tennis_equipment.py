from math import ceil, floor

price_one_raketa = float(input())
number_raketi = int(input())
number_chift_trainers = int(input())

one_chift_trainers = price_one_raketa * 1/6
price_trainers_raketi = price_one_raketa * number_raketi + one_chift_trainers * number_chift_trainers
other_equipment = price_trainers_raketi * 20/100

final_price = price_trainers_raketi + other_equipment

print(f"Price to be paid by Djokovic {floor(final_price * 1/8)}")
print(f"Price to be paid by sponsors {ceil(final_price * 7/8)}")