wanted_profit = float(input())

total_made_profit = 0
discount = 0
name_coctail = input()
while name_coctail != "Party!":
    number_coctails = int(input())

    price_coctail = len(name_coctail) * number_coctails


    if price_coctail % 2 != 0:
        discount = price_coctail * 25/100
        price_coctail -= discount

    total_made_profit += price_coctail

    if total_made_profit >= wanted_profit:

        break

    name_coctail = input()


if name_coctail == "Party!":
    print(f"We need {wanted_profit - total_made_profit:.2f} leva more.")
elif total_made_profit >= wanted_profit:
    print("Target acquired.")
print(f"Club income - {total_made_profit:.2f} leva.")

