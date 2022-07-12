number_days = int(input())
number_hours = int(input())

total_money = 0
parking_tax = 0
curr_money = 0

for day in range(1, number_days + 1):
    for hour in range(1, number_hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            parking_tax = 2.50
            curr_money += parking_tax

        elif day % 2 != 0 and hour % 2 == 0:
            parking_tax = 1.25
            curr_money += parking_tax
        else:
            parking_tax = 1
            curr_money += parking_tax

    total_money += curr_money
    print(f"Day: {day} - {curr_money:.2f} leva")
    curr_money = 0
print(f"Total: {total_money:.2f} leva")