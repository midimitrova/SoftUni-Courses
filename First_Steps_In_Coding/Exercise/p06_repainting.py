nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

price_for_nylon = (nylon + 2) * 1.50
price_for_paint = (paint + 10/100 * paint) * 14.50
price_for_thinner = thinner * 5
price_for_bags = 0.40
total_price = price_for_nylon + price_for_paint + price_for_thinner + price_for_bags
price_for_worker = (total_price * 30/100) * hours
final_price = total_price + price_for_worker

print(f"{final_price}")


