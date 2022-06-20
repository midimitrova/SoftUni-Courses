month = input()
number_nights = int(input())

price_apartment = 0
price_studio = 0

if month == "May" or month == "October":
    if number_nights > 14:
        price_studio = number_nights * 50
        price_studio = price_studio - price_studio * 30/100
        price_apartment = number_nights * 65
        price_apartment = price_apartment - price_apartment * 10/100
    elif number_nights > 7:
        price_studio = number_nights * 50
        price_studio = price_studio - price_studio * 5/100
        price_apartment = number_nights * 65
    else:
        price_studio = number_nights * 50
        price_apartment = number_nights * 65
elif month == "June" or month == "September":
    if number_nights > 14:
        price_studio = number_nights * 75.20
        price_studio = price_studio - price_studio * 20/100
        price_apartment = number_nights * 68.70
        price_apartment = price_apartment - price_apartment * 10/100
    else:
        price_studio = number_nights * 75.20
        price_apartment = number_nights * 68.70
elif month == "July" or month == "August":
    price_studio = number_nights * 76
    price_apartment = number_nights * 77
    if number_nights > 14:
        price_apartment = price_apartment - price_apartment * 10/100

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
