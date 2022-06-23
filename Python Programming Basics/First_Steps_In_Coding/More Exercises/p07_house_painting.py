x = float(input())
y = float(input())
h = float(input())

# for walls green paint
front_and_back_walls = (x * x) * 2
door = 1.2 * 2
front_and_back_walls_without_door = front_and_back_walls - door

side_walls = (x * y) * 2
windows = 1.5 * 1.5 * 2
side_walls_without_windows = side_walls - windows

total_area_walls = front_and_back_walls_without_door + side_walls_without_windows
needed_paint_walls = total_area_walls / 3.4

# for roof red paint
area1 = 2 * (x * y)
area2 = 2 * ((x * h) / 2)

total_area_roof = area1 + area2
needed_paint_roof = total_area_roof / 4.3

print("{:.2f}".format(needed_paint_walls))
print("{:.2f}".format(needed_paint_roof))