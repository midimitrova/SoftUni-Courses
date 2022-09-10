n = int(input())

capacity = 255

total_litres = 0

while n > 0:

    liters_of_water = int(input())

    total_litres += liters_of_water

    if total_litres > capacity:
        total_litres -= liters_of_water
        print("Insufficient capacity!")

    n -= 1

print(total_litres)