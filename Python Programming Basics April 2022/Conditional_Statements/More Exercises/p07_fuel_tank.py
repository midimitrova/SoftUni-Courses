type_fuel = input()
littre_fuel = int(input())

if littre_fuel >= 25:
    if type_fuel != "Diesel" and type_fuel != "Gas" and type_fuel != "Gasoline":
        print(f"Invalid fuel!")
    else:
        print(f"You have enough {type_fuel.lower()}.")
else:

    if type_fuel != "Diesel" and type_fuel != "Gas" and type_fuel != "Gasoline":
        print(f"Invalid fuel!")
    else:
        print(f"Fill your tank with {type_fuel.lower()}!")





