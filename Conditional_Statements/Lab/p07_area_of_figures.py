from math import pi
type_of_figure = input()
area = 0

if type_of_figure == "square":
    a = float(input())
    area = a * a
elif type_of_figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif type_of_figure == "circle":
    r = float(input())
    area = pi * r ** 2
elif type_of_figure == "triangle":
    h = float(input())
    a = float(input())
    area = (a * h) / 2

print("{:.3f}".format(area))

