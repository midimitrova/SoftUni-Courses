city = input()
type_package = input()
vip_discount = input()
number_days = int(input())

price_per_day = 0
discount = 0

if city == "Bansko" or city == "Borovets":
    if type_package == "withEquipment":
        price_per_day = 100
        discount = 0.1
    elif type_package == "noEquipment":
        price_per_day = 80
        discount = 0.05

elif city == "Varna" or city == "Burgas":
    if type_package == "withBreakfast":
        price_per_day = 130
        discount = 0.12
    elif type_package == "noBreakfast":
        price_per_day = 100
        discount = 0.07

total_price = price_per_day * number_days



if (city != "Bansko" and city != "Borovets" and city != "Varna" and city != "Burgas") \
        or (type_package != "withEquipment" and type_package != "noEquipment"
            and type_package != "withBreakfast" and type_package != "noBreakfast"):
    print(f"Invalid input!")
elif 1 <= number_days <= 7:
    if vip_discount == "yes":
        total_price -= total_price * discount
    elif vip_discount == "no":
        total_price
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
elif number_days > 7:
    total_price -= price_per_day
    if vip_discount == "yes":
        total_price -= total_price * discount
    elif vip_discount == "no":
        total_price
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
elif number_days < 1:
    print(f"Days must be positive number!")



