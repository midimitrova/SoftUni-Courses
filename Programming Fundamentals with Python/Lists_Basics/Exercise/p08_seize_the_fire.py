fire_level = input().split('#')
amount_of_water = int(input())

total_effort = 0
total_fire = 0
cnt_fire_items = 0

print('Cells:')

while True:
    for fire in fire_level:
        fire_items = fire.split(' = ')
        level = fire_items[0]
        needed_water = int(fire_items[1])
        cnt_fire_items += 1

        if amount_of_water < needed_water:
            continue

        if level == 'High' and needed_water in range(81, 126):
            amount_of_water -= needed_water
            total_effort += needed_water * 25 / 100
            total_fire += needed_water
            print(f' - {needed_water}')
        elif level == 'Medium' and needed_water in range(51, 81):
            amount_of_water -= needed_water
            total_effort += needed_water * 25 / 100
            total_fire += needed_water
            print(f' - {needed_water}')
        elif level == 'Low' and needed_water in range(1, 51):
            amount_of_water -= needed_water
            total_effort += needed_water * 25 / 100
            total_fire += needed_water
            print(f' - {needed_water}')
    if amount_of_water == 0 or cnt_fire_items == len(fire_level):
        break

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")