number_sea = int(input())
number_mountain = int(input())

cnt_sea = 0
cnt_mountain = 0
price = 0

total_price = 0
total_products = number_sea + number_mountain
command = input()

while command != "Stop":
    type_excursion = str(command)

    if type_excursion == "sea":
        price = 680
        cnt_sea += 1
        if cnt_sea <= number_sea:
            total_price += price
        else:
            cnt_sea -= 1
    elif type_excursion == "mountain":
        price = 499
        cnt_mountain += 1
        if cnt_mountain <= number_mountain:
            total_price += price
        else:
            cnt_mountain -= 1

    if total_products <= (cnt_sea + cnt_mountain):
        break


    command = input()



if total_products <= (cnt_sea + cnt_mountain):
    print(f"Good job! Everything is sold.")

print(f"Profit: {total_price} leva.")