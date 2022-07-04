fruit = input()
size_set = input()
number_sets = int(input())

price_one_set = 0
total_price = 0

if fruit == "Watermelon":
    if size_set == "small":
        price_one_set = 56 * 2

    elif size_set == "big":
        price_one_set = 28.70 * 5

elif fruit == "Mango":
    if size_set == "small":
        price_one_set = 36.66 * 2

    elif size_set == "big":
        price_one_set = 19.60 * 5

elif fruit == "Pineapple":
    if size_set == "small":
        price_one_set = 42.10 * 2

    elif size_set == "big":
        price_one_set = 24.80 * 5

elif fruit == "Raspberry":
    if size_set == "small":
        price_one_set = 20 * 2

    elif size_set == "big":
        price_one_set = 15.20 * 5


total_price = price_one_set * number_sets

if 400 <= total_price <= 1000:
    total_price -= total_price * 15/100
elif total_price > 1000:
    total_price -= total_price * 50/100

print(f"{total_price:.2f} lv.")











