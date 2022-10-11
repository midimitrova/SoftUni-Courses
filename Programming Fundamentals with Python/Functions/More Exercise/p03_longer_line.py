from math import floor


def coordinate_system(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


coord_x1 = float(input())
coord_y1 = float(input())
coord_x2 = float(input())
coord_y2 = float(input())
coord_x3 = float(input())
coord_y3 = float(input())
coord_x4 = float(input())
coord_y4 = float(input())

dist_x1_y1 = coordinate_system(coord_x1, coord_y1, 0, 0)
dist_x2_y2 = coordinate_system(coord_x2, coord_y2, 0, 0)
dist_x3_y3 = coordinate_system(coord_x3, coord_y3, 0, 0)
dist_x4_y4 = coordinate_system(coord_x4, coord_y4, 0, 0)

line1 = dist_x1_y1 + dist_x2_y2
line2 = dist_x3_y3 + dist_x4_y4

if line1 >= line2:
    if dist_x1_y1 <= dist_x2_y2:
        print(f'({floor(coord_x1)}, {floor(coord_y1)})({floor(coord_x2)}, {floor(coord_y2)})')
    else:
        print(f'({floor(coord_x2)}, {floor(coord_y2)})({floor(coord_x1)}, {floor(coord_y1)})')
elif line1 < line2:
    if dist_x3_y3 <= dist_x4_y4:
        print(f'({floor(coord_x3)}, {floor(coord_y3)})({floor(coord_x4)}, {floor(coord_y4)})')
    else:
        print(f'({floor(coord_x4)}, {floor(coord_y4)})({floor(coord_x3)}, {floor(coord_y3)})')
