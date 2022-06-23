w = float(input())
h = float(input())

if h >= 3 and w >= h and w <= 100:
 width_without_path  = h * 100 - 100
 number_desks_width = width_without_path // 70
 high_area = w * 100
 number_desks_high = high_area // 120
 total_desks = number_desks_width * number_desks_high -3
 print(total_desks)

else:
    print("Invalid data")
