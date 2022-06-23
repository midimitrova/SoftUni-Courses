projection = input()
row = int(input())
column = int(input())

income = row * column

if projection == "Premiere":
    print(f"{income * 12:.2f} leva")
elif projection == "Normal":
    print(f"{income * 7.50:.2f} leva")
elif projection == "Discount":
    print(f"{income * 5:.2f} leva")