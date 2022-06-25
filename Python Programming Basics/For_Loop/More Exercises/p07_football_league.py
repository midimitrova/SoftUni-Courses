capacity_stadium = int(input())
number_fans = int(input())

sector1 = 0
sector2 = 0
sector3 = 0
sector4 = 0

for fan in range(1, number_fans + 1):
    sector = input()

    if sector == "A":
        sector1 += 1
    elif sector == "B":
        sector2 += 1
    elif sector == "V":
        sector3 += 1
    elif sector == "G":
        sector4 += 1

print(f"{(sector1 / number_fans) * 100:.2f}%")
print(f"{(sector2 / number_fans) * 100:.2f}%")
print(f"{(sector3 / number_fans) * 100:.2f}%")
print(f"{(sector4 / number_fans) * 100:.2f}%")
print(f"{(number_fans / capacity_stadium) * 100:.2f}%")