number_days = int(input())
number_hours = int(input())

total_sum = 0
price = 0
day_cnt = 0
curr_price = 0

for day in range(1, number_days + 1):
    for hour in range(1, number_hours + 1):

        if day % 2 == 0 and hour % 2 != 0:
            price = 2.50
            curr_price += price

        elif day % 2 != 0 and hour % 2 == 0:
            price = 1.25
            curr_price += price
        else:
            price = 1
            curr_price += price

    total_sum += curr_price
    day_cnt += 1
    print(f"Day: {day_cnt} - {curr_price:.2f} leva")

    curr_price = 0

print(f"Total: {total_sum:.2f} leva")

