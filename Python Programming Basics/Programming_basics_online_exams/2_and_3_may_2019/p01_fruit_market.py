price_strawberry = float(input())
number_bananas_kg = float(input())
number_orange_kg = float(input())
number_rasberry_kg = float(input())
number_strawberry_kg = float(input())

price_rasberry = price_strawberry - price_strawberry * 50/100
price_orange = price_rasberry - price_rasberry * 40/100
price_bananas = price_rasberry - price_rasberry * 80/100

total_price = price_strawberry * number_strawberry_kg + price_bananas * number_bananas_kg\
              + price_orange * number_orange_kg + price_rasberry * number_rasberry_kg

print(f"{total_price:.2f}")