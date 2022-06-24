age_lili = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toy_count = 0
money_given = 0
saved_money = 0
sum_money = 0

for age in range(1, age_lili + 1):
    if age % 2 == 0:
        money_given = (age * 5) - 1
        sum_money += money_given

    else:
        toy_count += 1

saved_money = (toy_count * toy_price) + sum_money

if saved_money >= washing_machine_price:
    print(f"Yes! {saved_money - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - saved_money:.2f}")