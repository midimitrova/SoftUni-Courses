season = input()
kilometres_per_month = float(input())

price_per_km = 0

if kilometres_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.75
    elif season == "Summer":
        price_per_km = 0.90
    elif season == "Winter":
        price_per_km = 1.05
elif 5000 < kilometres_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.95
    elif season == "Summer":
        price_per_km = 1.10
    elif season == "Winter":
        price_per_km = 1.25
elif 10000 < kilometres_per_month <= 20000:
    price_per_km = 1.45

price = kilometres_per_month * price_per_km * 4
price_after_tax = price - price * 10/100

print(f"{price_after_tax:.2f}")