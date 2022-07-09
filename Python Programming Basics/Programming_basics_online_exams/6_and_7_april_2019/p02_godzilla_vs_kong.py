budget = float(input())
number_workers = int(input())
price_clothes_worker = float(input())

decor = budget * 10/100

total_price_clothes = number_workers * price_clothes_worker

if number_workers > 150:
    discount = total_price_clothes * 10/100
    total_price_clothes -= discount

total_price = total_price_clothes + decor

if total_price > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {total_price - budget:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {budget - total_price:.2f} leva left.")