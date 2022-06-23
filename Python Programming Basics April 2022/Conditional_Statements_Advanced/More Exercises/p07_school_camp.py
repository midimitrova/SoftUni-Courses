season = input()
type_group = input()
number_student = int(input())
number_nights = int(input())

price_per_night = 0
type_sport = ""
discount = 0

if season == "Winter":
    if type_group == "girls":
        price_per_night = 9.60
        type_sport = "Gymnastics"
    elif type_group == "boys":
        price_per_night = 9.60
        type_sport = "Judo"
    elif type_group == "mixed":
        price_per_night = 10
        type_sport = "Ski"
elif season == "Spring":
    if type_group == "girls":
        price_per_night = 7.20
        type_sport = "Athletics"
    elif type_group == "boys":
        price_per_night = 7.20
        type_sport = "Tennis"
    elif type_group == "mixed":
        price_per_night = 9.50
        type_sport = "Cycling"
elif season == "Summer":
    if type_group == "girls":
        price_per_night = 15
        type_sport = "Volleyball"
    elif type_group == "boys":
        price_per_night = 15
        type_sport = "Football"
    elif type_group == "mixed":
        price_per_night = 20
        type_sport = "Swimming"

if number_student >= 50:
    discount = 0.5
elif 20 <= number_student < 50:
    discount = 0.15
elif 10 <= number_student < 20:
    discount = 0.05

price = number_student * number_nights * price_per_night
price_after_discount = price - price * discount

print(f"{type_sport} {price_after_discount:.2f} lv.")