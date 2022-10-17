number_of_rooms = int(input())

left_chairs = 0
are_left = True

for room in range(1, number_of_rooms + 1):
    chairs, visitors = input().split()
    visitors = int(visitors)
    difference = abs(len(chairs) - visitors)

    if len(chairs) < visitors:
        print(f"{difference} more chairs needed in room {room}")
        are_left = False
    else:
        left_chairs += difference


if are_left:
    print(f"Game On, {left_chairs} free chairs left")
