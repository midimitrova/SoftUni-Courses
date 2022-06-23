from math import ceil, floor


number_magnolii = int(input())
number_zumbuli = int(input())
number_roses = int(input())
number_kaktus = int(input())
price_present = float(input())

price_magnolii = number_magnolii * 3.25
price_zumbuli = number_zumbuli * 4
price_roses = number_roses * 3.50
price_kaktus = number_kaktus * 8

total_price = price_magnolii + price_zumbuli + price_roses + price_kaktus
tax = total_price * 0.05
final_price = total_price - tax

if final_price >= price_present:
    print(f"She is left with {floor(final_price - price_present)} leva.")
else:
    print(f"She will have to borrow {ceil(price_present - final_price)} leva.")