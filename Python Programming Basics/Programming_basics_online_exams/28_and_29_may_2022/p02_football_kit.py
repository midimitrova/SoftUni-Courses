price_tshirt = float(input())
needed_money_to_win = float(input())

price_shorts = price_tshirt * 75/100
price_socks = price_shorts * 20/100
price_shoes = (price_tshirt + price_shorts) * 2
discount = 0.15

total_sum = (price_tshirt + price_shorts + price_socks + price_shoes) - \
            (price_tshirt + price_shorts + price_socks + price_shoes) * discount

if total_sum >= needed_money_to_win:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum:.2f} lv.")
else:
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {needed_money_to_win - total_sum:.2f} lv. more.")