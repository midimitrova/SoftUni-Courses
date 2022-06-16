city = input()
volume = float(input())

if city == "Sofia":
    if 0 <= volume <= 500:
        print(f"{volume * 5 / 100:.2f}")
    elif 500 < volume <= 1000:
        print(f"{volume * 7 / 100:.2f}")
    elif 1000 < volume <= 10000:
        print(f"{volume * 8 / 100:.2f}")
    elif volume > 10000:
        print(f"{volume * 12 / 100:.2f}")
    else:
        print("error")

elif city == "Varna":
    if 0 <= volume <= 500:
        print(f"{volume * 4.5 / 100:.2f}")
    elif 500 < volume <= 1000:
        print(f"{volume * 7.5 / 100:.2f}")
    elif 1000 < volume <= 10000:
        print(f"{volume * 10 / 100:.2f}")
    elif volume > 10000:
        print(f"{volume * 13 / 100:.2f}")
    else:
        print("error")


elif city == "Plovdiv":
    if 0 <= volume <= 500:
        print(f"{volume * 5.5 / 100:.2f}")
    elif 500 < volume <= 1000:
        print(f"{volume * 8 / 100:.2f}")
    elif 1000 < volume <= 10000:
        print(f"{volume * 12 / 100:.2f}")
    elif volume > 10000:
        print(f"{volume * 14.5 / 100:.2f}")
    else:
        print("error")
else:
    print("error")