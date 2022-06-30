number_floor = int(input())
number_rooms = int(input())
flat_number = 0
flat_name = ''


for floor in range(number_floor, 0, -1):
    for flat in range(number_rooms):
        flat_number = floor * 10 + flat

        if floor == number_floor:
            flat_name = f"L{flat_number}"

        elif floor % 2 == 0:
            flat_name = f"O{flat_number}"

        else:
            flat_name = f"A{flat_number}"

        print(flat_name, end=" ")

    print()
