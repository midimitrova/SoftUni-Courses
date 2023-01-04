box_of_clothes = [int(x) for x in input().split()]
capacity_of_one_rack = int(input())

current_rack_capacity = capacity_of_one_rack
racks_quantity = 1

while box_of_clothes:
    current_item = box_of_clothes[-1]
    if current_rack_capacity >= current_item:
        current_rack_capacity -= current_item
        box_of_clothes.pop()
    else:
        racks_quantity += 1
        current_rack_capacity = capacity_of_one_rack

print(racks_quantity)
