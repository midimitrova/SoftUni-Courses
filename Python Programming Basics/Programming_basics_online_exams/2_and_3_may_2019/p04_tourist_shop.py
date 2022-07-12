budget = float(input())

product_cnt = 0
total_price = 0


name_product = input()
while name_product != "Stop":
    price_product = float(input())

    product_cnt += 1
    if product_cnt % 3 == 0:
        price_product = price_product / 2

    total_price += price_product

    if budget < total_price:
        break
    name_product = input()
if name_product == "Stop":
    print(f"You bought {product_cnt} products for {total_price:.2f} leva.")
elif budget < total_price:
    print("You don't have enough money!")
    print(f"You need {abs(budget - total_price):.2f} leva!")



