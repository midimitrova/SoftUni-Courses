budget = float(input())
season = input()

price = 0
location = ""
accommodation = ""

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 65/100
    elif season == "Winter":
        location = "Morocco"
        price = budget * 45/100
elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 80/100
    elif season == "Winter":
        location = "Morocco"
        price = budget * 60/100
elif budget > 3000:
    accommodation = "Hotel"
    price = budget * 90/100
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"

print(f"{location} - {accommodation} - {0.001 + price:.2f}")