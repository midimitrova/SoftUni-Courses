rent = int(input())

price_figurines = rent - rent * 30/100
price_catering = price_figurines - price_figurines * 15/100
price_sound = price_catering * 1/2

total_price = rent + price_catering + price_figurines + price_sound

print(f"{total_price:.2f}")