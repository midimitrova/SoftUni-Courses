collections_of_items = input().split('|')
budget = float(input())
ticket = 150
total_bought_items = []
cnt_bought_items = 0
while True:
    for collection in collections_of_items:
        bought_items = collection.split('->')
        item = bought_items[0]
        price = float(bought_items[1])
        cnt_bought_items += 1

        if budget < price:
            continue

        if item == 'Clothes' and price <= 50.00:
            budget -= price
            total_bought_items.append(price)
        elif item == 'Shoes' and price <= 35.00:
            budget -= price
            total_bought_items.append(price)
        elif item == 'Accessories' and price <= 20.50:
            budget -= price
            total_bought_items.append(price)

    if budget == 0 or cnt_bought_items == len(collections_of_items):
        break

new_prices = []
for price in total_bought_items:
    new_price = price * 40 / 100 + price
    new_prices.append(new_price)
    print(f"{new_price:.2f}", end=' ')
print()
sum_old_prices = sum(total_bought_items)
sum_new_prices = sum(new_prices)
profit = sum_new_prices - sum_old_prices
print(f"Profit: {profit:.2f}")

new_budget = budget + sum_new_prices
if new_budget >= ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
