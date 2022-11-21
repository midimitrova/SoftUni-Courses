number_of_cars = int(input())

collection_of_cars = {}

for _ in range(number_of_cars):
    cars = input().split('|')
    model = cars[0]
    mileage = int(cars[1])
    fuel_available = int(cars[2])
    collection_of_cars[model] = [mileage, fuel_available]

data = input().split(' : ')
while data[0] != 'Stop':
    command = data[0]

    if command == 'Drive':
        car_model = data[1]
        distance = int(data[2])
        fuel = int(data[3])
        if fuel <= collection_of_cars[car_model][1]:
            collection_of_cars[car_model][0] += distance
            collection_of_cars[car_model][1] -= fuel
            print(f'{car_model} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        else:
            print('Not enough fuel to make that ride')
        if collection_of_cars[car_model][0] >= 100000:
            print(f'Time to sell the {car_model}!')
            collection_of_cars.pop(car_model)
    elif command == 'Refuel':
        car_model = data[1]
        fuel = int(data[2])
        needed_fuel = 75 - collection_of_cars[car_model][1]
        collection_of_cars[car_model][1] += fuel
        if collection_of_cars[car_model][1] >= 75:
            collection_of_cars[car_model][1] = 75
            print(f'{car_model} refueled with {needed_fuel} liters')
        else:
            print(f'{car_model} refueled with {fuel} liters')
    elif command == 'Revert':
        car_model = data[1]
        kilometres = int(data[2])
        collection_of_cars[car_model][0] -= kilometres
        if collection_of_cars[car_model][0] < 10000:
            collection_of_cars[car_model][0] = 10000
        else:
            print(f'{car_model} mileage decreased by {kilometres} kilometers')

    data = input().split(' : ')

for car_model, car_info in collection_of_cars.items():
    print(
        f'{car_model} -> Mileage: {collection_of_cars[car_model][0]} kms, Fuel in the tank:'
        f' {collection_of_cars[car_model][1]} lt.')
