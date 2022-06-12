budjet_film = float(input())
number_of_people = int(input())
price_for_clothing_for_one_person = float(input())

decor = budjet_film * 0.1
price_for_clothing = number_of_people * price_for_clothing_for_one_person

if number_of_people > 150:
    discount = price_for_clothing * 0.1
    price_for_clothing = price_for_clothing - discount

total_sum = decor + price_for_clothing

if total_sum > budjet_film:
    print(f"Not enough money!\nWingard needs {total_sum - budjet_film:.2f} leva more.")
else:
    print(f"Action!\nWingard starts filming with {budjet_film - total_sum:.2f} leva left.")