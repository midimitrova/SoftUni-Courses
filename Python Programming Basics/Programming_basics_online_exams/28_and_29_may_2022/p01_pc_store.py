price_pr_dollars = float(input())
price_video_dollars = float(input())
price_ram_dollars = float(input())
number_ram = int(input())
discount = float(input())


dollar_to_lev = 1.57

price_lev_pr = price_pr_dollars * dollar_to_lev
price_lev_video = price_video_dollars * dollar_to_lev
price_lev_ram = (price_ram_dollars * dollar_to_lev) * number_ram

price_with_discount_pr = price_lev_pr - price_lev_pr * discount
price_with_discount_video = price_lev_video - price_lev_video * discount

total_price = price_with_discount_video + price_with_discount_pr + price_lev_ram
print(f"Money needed - {total_price:.2f} leva.")