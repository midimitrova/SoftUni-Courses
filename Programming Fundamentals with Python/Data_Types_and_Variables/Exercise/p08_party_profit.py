people = int(input())
days = int(input())

earn_money = 0
money_for_food = 0
money_for_water = 0

for day in range(1, days + 1):

    if day % 10 == 0:
        people -= 2

    if day % 15 == 0:

        people += 5


    earn_money += 50
    money_for_food += people * 2


    if day % 3 == 0:
        money_for_water += people * 3

    if day % 5 == 0:

        earn_money += 20 * people
        if day % 3 == 0:
            money_for_food += people * 2



print(f"{people} companions received {(earn_money - money_for_food - money_for_water) // people} coins each.")




