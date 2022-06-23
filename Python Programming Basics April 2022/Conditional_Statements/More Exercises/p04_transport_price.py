kilometre = int(input())
period_day = input()

entry_tax_taxi = 0.70
day_taxi = 0.79
night_taxi = 0.90
day_night_bus = 0.09
day_night_train = 0.06

if kilometre < 20:
    if period_day == "day":
     total_price = entry_tax_taxi + day_taxi * kilometre
    elif period_day == "night":
     total_price = entry_tax_taxi + kilometre * night_taxi
elif kilometre >= 100:
    total_price = kilometre * day_night_train
elif kilometre >= 20:
    total_price = kilometre * day_night_bus

print(f"{total_price:.2f}")


