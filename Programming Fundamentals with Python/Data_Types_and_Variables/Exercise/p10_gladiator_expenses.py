lost_fights_count = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())


helmet_cnt = 0
sword_cnt = 0
shield_cnt = 0
armor_cnt = 0

for loose in range(1, lost_fights_count + 1):

    if loose % 2 == 0:
        helmet_cnt += 1

    if loose % 3 == 0:
        sword_cnt += 1

    if loose % 6 == 0:
        shield_cnt += 1

        if shield_cnt % 2 == 0:
            armor_cnt += 1

total = helmet_price * helmet_cnt + sword_price * sword_cnt + shield_price * shield_cnt + armor_price * armor_cnt

print(f"Gladiator expenses: {total:.2f} aureus")





