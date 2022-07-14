number = float(input())
entry_unit = input()
exit_unit = input()

this_dict = dict(m=1, mm=1000, cm=100, mi=0.000621371192, inches =39.3700787, km = 0.001, ft = 3.2808399, yd = 1.0936133)
result = number / this_dict[entry_unit] * this_dict[exit_unit]
print(f'{result} {exit_unit}')

