year_tax = int(input())

price_trainers = year_tax - year_tax * 40/100
price_clothes = price_trainers - price_trainers * 20/100
price_ball = price_clothes * 1/4
price_accessories = price_ball * 1/5

total_price = year_tax + price_trainers + price_clothes + price_ball + price_accessories

print(f"{total_price:.2f}")