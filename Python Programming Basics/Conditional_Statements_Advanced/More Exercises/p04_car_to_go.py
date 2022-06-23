budget = float(input())
season = input()

class_car = ""
type_car = ""
price_car = 0

if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        price_car = budget * 35/100
    elif season == "Winter":
        type_car = "Jeep"
        price_car = budget * 65/100
elif 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        price_car = budget * 45/100
    elif season == "Winter":
        type_car = "Jeep"
        price_car = budget * 80/100
elif budget > 500:
    class_car = "Luxury class"
    type_car = "Jeep"
    price_car = budget * 90/100

print(f"{class_car}")
print(f"{type_car} - {price_car:.2f}")