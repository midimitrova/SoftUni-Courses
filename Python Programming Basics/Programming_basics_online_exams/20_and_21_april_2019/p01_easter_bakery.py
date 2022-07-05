price_flour_kg = float(input())
flour_kg = float(input())
kg_sugar = float(input())
number_kori_eggs = int(input())
package_maq = int(input())

price_sugar_kg = price_flour_kg - price_flour_kg * 25/100
price_kora_egg = price_flour_kg + price_flour_kg * 10/100
price_package_maq = price_sugar_kg - price_sugar_kg * 80/100

total_price = price_flour_kg * flour_kg + price_sugar_kg * kg_sugar + \
              price_kora_egg * number_kori_eggs + price_package_maq * package_maq

print(f"{total_price:.2f}")