money = float(input())
year_to_living = int(input())

even_sum = 0
odd_sum = 0
ivan_years = 18

for year in range(1800, year_to_living + 1, 1):

    if year % 2 == 0:
        even_sum = 12000
        money -= even_sum
    else:
        odd_sum = 12000 + (50 * ivan_years)
        money -= odd_sum
    ivan_years += 1

if money >= 0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else:
    print(f"He will need {abs(money):.2f} dollars to survive.")