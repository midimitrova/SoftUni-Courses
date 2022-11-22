data = input().split('||')
pirate_target = {}

while data[0] != 'Sail':
    city = data[0]
    population = int(data[1])
    gold = int(data[2])
    if city not in pirate_target.keys():
        pirate_target[city] = [population, gold]
    else:
        pirate_target[city][0] += population
        pirate_target[city][1] += gold

    data = input().split('||')

command = input().split('=>')

while command[0] != 'End':
    current_command = command[0]

    if current_command == 'Plunder':
        town = command[1]
        people = int(command[2])
        current_gold = int(command[3])
        pirate_target[town][0] -= people
        pirate_target[town][1] -= current_gold

        print(f'{town} plundered! {current_gold} gold stolen, {people} citizens killed.')

        if pirate_target[town][0] <= 0 or pirate_target[town][1] <= 0:
            print(f'{town} has been wiped off the map!')
            pirate_target.pop(town)

    elif current_command == 'Prosper':
        town = command[1]
        current_gold = int(command[2])
        if current_gold < 0:
            print('Gold added cannot be a negative number!')
        else:
            pirate_target[town][1] += current_gold
            print(f'{current_gold} gold added to the city treasury. {town} now has {pirate_target[town][1]} gold.')

    command = input().split('=>')

if pirate_target:
    print(f'Ahoy, Captain! There are {len(pirate_target)} wealthy settlements to go to:')
    for town, value in pirate_target.items():
        print(f'{town} -> Population: {pirate_target[town][0]} citizens, Gold: {pirate_target[town][1]} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
