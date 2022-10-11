from math import floor


def coordinate_system(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


coord_x1 = float(input())
coord_y1 = float(input())
coord_x2 = float(input())
coord_y2 = float(input())

dist_x1_y1 = coordinate_system(coord_x1, coord_y1, 0, 0)
dist_x2_y2 = coordinate_system(coord_x2, coord_y2, 0, 0)
if dist_x1_y1 > dist_x2_y2:
    print(tuple([floor(coord_x2), floor(coord_y2)]))
else:
    print(tuple([floor(coord_x1), floor(coord_y1)]))
