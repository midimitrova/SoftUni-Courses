number_sold_games = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0

for _ in range(1, number_sold_games + 1):
    name_game = input()

    if name_game == "Hearthstone":
        p1 += 1
    elif name_game == "Fornite":
        p2 += 1
    elif name_game == "Overwatch":
        p3 += 1
    else:
        p4 += 1

p1 = (p1 / number_sold_games) * 100
p2 = (p2 / number_sold_games) * 100
p3 = (p3 / number_sold_games) * 100
p4 = (p4 / number_sold_games) * 100

print(f"Hearthstone - {p1:.2f}%")
print(f"Fornite - {p2:.2f}%")
print(f"Overwatch - {p3:.2f}%")
print(f"Others - {p4:.2f}%")