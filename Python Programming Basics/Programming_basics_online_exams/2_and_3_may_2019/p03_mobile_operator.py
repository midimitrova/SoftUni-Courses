term_contract = input()
type_contract = input()
added_internet = input()
number_month_paying = int(input())

price_per_month = 0
price_internet = 0

if type_contract == "Small":
    if term_contract == "one":
        price_per_month = 9.98
    elif term_contract == "two":
        price_per_month = 8.58
elif type_contract == "Middle":
    if term_contract == "one":
        price_per_month = 18.99
    elif term_contract == "two":
        price_per_month = 17.09
elif type_contract == "Large":
    if term_contract == "one":
        price_per_month = 25.98
    elif term_contract == "two":
        price_per_month = 23.59
elif type_contract == "ExtraLarge":
    if term_contract == "one":
        price_per_month = 35.99
    elif term_contract == "two":
        price_per_month = 31.79

if added_internet == "yes":
    if price_per_month <= 10:
        price_internet = 5.50
    elif price_per_month <= 30:
        price_internet = 4.35
    elif price_per_month > 30:
        price_internet = 3.85

total_price = (price_per_month + price_internet) * number_month_paying

if term_contract == "two":
    total_price -= total_price * 3.75/100

print(f"{total_price:.2f} lv.")