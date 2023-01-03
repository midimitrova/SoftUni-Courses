from collections import deque

water_quantity = int(input())
name = input()
line = deque()
while name != 'Start':
    line.append(name)
    name = input()

command = input()

while command != 'End':
    if command.isdigit():
        name = line.popleft()
        needed_water = int(command)
        if water_quantity >= needed_water:
            print(f'{name} got water')
            water_quantity -= needed_water
        else:
            print(f'{name} must wait')
    else:
        _, liters = command.split()
        liters = int(liters)
        water_quantity += liters
    command = input()

print(f'{water_quantity} liters left')
