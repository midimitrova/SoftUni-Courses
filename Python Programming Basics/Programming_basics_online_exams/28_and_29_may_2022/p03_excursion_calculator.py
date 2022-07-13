number_people = int(input())
season = input()

discount = 0.15
increase = 0.08
price = 0
total_price = 0

if season == "spring":
    if number_people <= 5:
        price = 50
        total_price = number_people * price
    elif number_people > 5:
        price = 48
        total_price = number_people * price
elif season == "summer":
    if number_people <= 5:
        price = 48.50
        total_price = (number_people * price) - ((number_people * price) * discount)
    elif number_people > 5:
        price = 45
        total_price = (number_people * price) - ((number_people * price) * discount)
elif season == "autumn":
    if number_people <= 5:
        price = 60
        total_price = number_people * price
    elif number_people > 5:
        price = 49.50
        total_price = number_people * price
elif season == "winter":
    if number_people <= 5:
        price = 86
        total_price = (number_people * price) + ((number_people * price) * increase)
    elif number_people > 5:
        price = 85
        total_price = (number_people * price) + ((number_people * price) * increase)

print(f"{total_price:.2f} leva.")