budget = float(input())
season = input()

destination = ""
holiday = ""
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        holiday = "Camp"
        price = budget * 30/100
    elif season == "winter":
        holiday = "Hotel"
        price = budget * 70/100

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        holiday = "Camp"
        price = budget * 40/100
    elif season == "winter":
        holiday = "Hotel"
        price = budget * 80/100

elif budget > 1000:
    destination = "Europe"
    if season == "summer" or season == "winter":
        holiday = "Hotel"
        price = budget * 90/100

print(f"Somewhere in {destination}")
print(f"{holiday} - {price:.2f}")
