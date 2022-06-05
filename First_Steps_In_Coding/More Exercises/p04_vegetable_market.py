price_for_kg_vegitables = float(input())
price_for_kg_fruits = float(input())
total_kg_vegitables = int(input())
total_kg_fruits = int(input())

total_price_vegitables = price_for_kg_vegitables * total_kg_vegitables
total_price_fruits = price_for_kg_fruits * total_kg_fruits

total_price = (total_price_vegitables + total_price_fruits) / 1.94
print("{:.2f}".format(total_price))