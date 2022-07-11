budget = float(input())

price_actor = 0

name = input()
while name != "ACTION":

    lenght = len(name)

    if lenght <= 15:
        price = float(input())
        budget -= price

    elif lenght > 15:
        price_actor = budget * 20 / 100
        budget -= price_actor

    if budget < 0:
        break
    name = input()
if budget >= 0:
    print(f"We are left with {budget:.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")

