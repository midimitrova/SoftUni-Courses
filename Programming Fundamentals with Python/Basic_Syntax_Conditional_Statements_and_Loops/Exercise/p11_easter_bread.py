budget = float(input())
price_flour_per_one_kg = float(input())


price_for_one_pack_eggs = price_flour_per_one_kg * 75/100
price_for_one_litre_milk = price_flour_per_one_kg + price_flour_per_one_kg * 25/100
price_needed_milk = price_for_one_litre_milk / 4

price_for_one_loaf = price_for_one_pack_eggs + price_flour_per_one_kg + price_needed_milk

colored_eggs = 0
loaf_cnt = 0

while True:

    budget -= price_for_one_loaf

    if budget < 0:
        break

    loaf_cnt += 1
    colored_eggs += 3

    if loaf_cnt % 3 == 0:
        colored_eggs -= (loaf_cnt - 2)


if budget < 0:
    print(f"You made {loaf_cnt} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget + price_for_one_loaf:.2f}BGN left.")
else:
    print(f"You made {loaf_cnt} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

