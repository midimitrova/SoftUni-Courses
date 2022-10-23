from math import ceil

budget = float(input())
students = int(input())
price_package_flour = float(input())
price_one_egg = float(input())
price_one_apron = float(input())

free_packages = 0
for student in range(1, students + 1):
    if student % 5 == 0:
        free_packages += 1

total_price = (price_package_flour * (students - free_packages)) + (10 * price_one_egg * students)\
              + price_one_apron * ceil(students + students * 0.2)

if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{total_price - budget:.2f}$ more needed.")
