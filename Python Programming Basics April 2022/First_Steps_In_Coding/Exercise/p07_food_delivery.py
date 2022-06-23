chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

price_for_chicken_menu = chicken_menu * 10.35
price_for_fish_menu = fish_menu * 12.40
price_for_vegan_menu = vegan_menu * 8.15
delivery = 2.50
total_price_before_discount = price_for_chicken_menu + price_for_fish_menu + price_for_vegan_menu
dessert = total_price_before_discount * 20/100
final_price = total_price_before_discount + dessert + delivery
print(final_price)