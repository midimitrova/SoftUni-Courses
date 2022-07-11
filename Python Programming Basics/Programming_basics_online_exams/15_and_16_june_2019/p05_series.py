budget = float(input())
number_serials = int(input())

price = 0
total_sum = 0

for i in range(1, number_serials + 1):
    name = input()
    price_serial = float(input())

    if name == "Thrones":
        price = price_serial - price_serial * 50/100
        total_sum += price
    elif name == "Lucifer":
        price = price_serial - price_serial * 40/100
        total_sum += price
    elif name == "Protector":
        price = price_serial - price_serial * 30/100
        total_sum += price
    elif name == "TotalDrama":
        price = price_serial - price_serial * 20/100
        total_sum += price
    elif name == "Area":
        price = price_serial - price_serial * 10/100
        total_sum += price
    else:
        price = price_serial
        total_sum += price

if budget >= total_sum:
    print(f"You bought all the series and left with {budget - total_sum:.2f} lv.")
else:
    print(f"You need {total_sum - budget:.2f} lv. more to buy the series!")