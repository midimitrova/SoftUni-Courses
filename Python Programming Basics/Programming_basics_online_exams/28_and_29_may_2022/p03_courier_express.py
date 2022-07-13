shipment_weight = float(input())
type_service = input()
distance_in_km = int(input())

price = 0
total_price = 0
price_without_markup = 0
price_with_markup = 0

if shipment_weight < 1:
    price = 3 / 100
    if type_service == "standard":
        total_price = distance_in_km * price
    elif type_service == "express":
        price_without_markup = distance_in_km * price
        price_with_markup = shipment_weight * (price * 80/100) * distance_in_km
        total_price = price_without_markup + price_with_markup
elif 1 <= shipment_weight < 10:
    price = 5 / 100
    if type_service == "standard":
        total_price = distance_in_km * price
    elif type_service == "express":
        price_without_markup = distance_in_km * price
        price_with_markup = shipment_weight * (price * 40/100) * distance_in_km
        total_price = price_without_markup + price_with_markup
elif 10 <= shipment_weight < 40:
    price = 10 / 100
    if type_service == "standard":
        total_price = distance_in_km * price
    elif type_service == "express":
        price_without_markup = distance_in_km * price
        price_with_markup = shipment_weight * (price * 5/100) * distance_in_km
        total_price = price_without_markup + price_with_markup
elif 40 <= shipment_weight < 90:
    price = 15 / 100
    if type_service == "standard":
        total_price = distance_in_km * price
    elif type_service == "express":
        price_without_markup = distance_in_km * price
        price_with_markup = shipment_weight * (price * 2/100) * distance_in_km
        total_price = price_without_markup + price_with_markup
elif 90 <= shipment_weight < 150:
    price = 20 / 100
    if type_service == "standard":
        total_price = distance_in_km * price
    elif type_service == "express":
        price_without_markup = distance_in_km * price
        price_with_markup = shipment_weight * (price * 1/100) * distance_in_km
        total_price = price_without_markup + price_with_markup

print(f"The delivery of your shipment with weight of {shipment_weight:.3f} kg. would cost {total_price:.2f} lv.")
