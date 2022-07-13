days = int(input())

total_quantity = 0
total_degrees = 0
average_degrees = 0

for day in range(1, days + 1):
    quantity_drink = float(input())
    degrees_drink = float(input())

    total_quantity += quantity_drink
    curr_degrees_drink = quantity_drink * degrees_drink
    total_degrees += curr_degrees_drink

average_degrees = total_degrees / total_quantity

print(f"Liter: {total_quantity:.2f}")
print(f"Degrees: {average_degrees:.2f}")


if average_degrees < 38:
    print(f"Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print(f"Super!")
elif average_degrees > 42:
    print(f"Dilution with distilled water!")