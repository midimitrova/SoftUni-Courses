months_paid = int(input())

water_price = 20
internet_price = 15
total_el_price = 0
total_electricity_price = 0

for price in range(1, months_paid + 1):
    electricity_price = float(input())
    total_el_price += electricity_price

total_water_price = months_paid * water_price
total_electricity_price = total_el_price
total_internet_price = months_paid * internet_price
total_other_price = total_electricity_price + months_paid * (water_price + internet_price) + \
                    (total_electricity_price + months_paid * (water_price + internet_price)) * 20/100
total_paid = total_other_price + total_internet_price + total_water_price + total_electricity_price
average_paid = total_paid / months_paid

print(f"Electricity: {total_electricity_price:.2f} lv")
print(f"Water: {total_water_price:.2f} lv")
print(f"Internet: {total_internet_price:.2f} lv")
print(f"Other: {total_other_price:.2f} lv")
print(f"Average: {average_paid:.2f} lv")