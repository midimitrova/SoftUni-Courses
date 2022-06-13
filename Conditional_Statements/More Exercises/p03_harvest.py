import math

vine_area = int(input())
grape_for_one_metre = float(input())
needed_vine = int(input())
number_workers = int(input())


total_vine = vine_area * grape_for_one_metre
production_vine = total_vine * 0.4
vine_littre = production_vine / 2.5
left_vine = vine_littre - needed_vine

if vine_littre < needed_vine:
    print(f"It will be a tough winter! More {math.floor(needed_vine - vine_littre)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(vine_littre)} liters.")
    print(f"{math.ceil(left_vine)} liters left -> "
          f"{math.ceil(left_vine / number_workers)} liters per person.")