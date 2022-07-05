size_egg = input()
colour_egg = input()
number_sets_eggs = int(input())

price = 0


if colour_egg == "Red":
    if size_egg == "Large":
        price = 16
    elif size_egg == "Medium":
        price = 13
    elif size_egg == "Small":
        price = 9
elif colour_egg == "Green":
    if size_egg == "Large":
        price = 12
    elif size_egg == "Medium":
        price = 9
    elif size_egg == "Small":
        price = 8
elif colour_egg == "Yellow":
    if size_egg == "Large":
        price = 9
    elif size_egg == "Medium":
        price = 7
    elif size_egg == "Small":
        price = 5

total_price = price * number_sets_eggs
expense = total_price * 35/100
total_price -= expense

print(f"{total_price:.2f} leva.")