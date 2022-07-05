number_clients = int(input())

price_basket = 1.50
price_wreath = 3.80
price_chocolate_bunny = 7

products_cnt = 0
price = 0
total_money = 0
discount = 0.2
curr_price = 0

for client in range(1, number_clients + 1):
    command = input()
    while command != "Finish":
        if command == "basket":
            products_cnt += 1
            price = price_basket
        elif command == "wreath":
            products_cnt += 1
            price = price_wreath
        elif command == "chocolate bunny":
            products_cnt += 1
            price = price_chocolate_bunny

        curr_price += price

        command = input()
    if products_cnt % 2 == 0:
        curr_price -= curr_price * discount

    if command == "Finish":
        print(f"You purchased {products_cnt} items for {curr_price:.2f} leva.")
    total_money += curr_price
    curr_price = 0
    products_cnt = 0

print(f"Average bill per client is: {(total_money / number_clients):.2f} leva.")


