vehicles = input().split('>>')

family_tax = 50
heavyDuty_tax = 80
sports_tax = 100
total_tax = 0
total_tax_family = 0
total_tax_heavyDuty = 0
total_tax_sports = 0
for i in range(len(vehicles)):
    car = vehicles[i]
    type_car, years_for_tax, kilometres = car.split()
    years_for_tax = int(years_for_tax)
    kilometres = int(kilometres)

    if type_car not in ['family', 'heavyDuty', 'sports']:
        print("Invalid car type.")
        continue

    if type_car == 'family':
        kilometres_to_charge = (kilometres // 3000) * 12
        total_tax_family = kilometres_to_charge + (family_tax - years_for_tax * 5)
        print(f'A {type_car} car will pay {total_tax_family:.2f} euros in taxes.')
    elif type_car == 'heavyDuty':
        kilometres_to_charge = (kilometres // 9000) * 14
        total_tax_heavyDuty = kilometres_to_charge + (heavyDuty_tax - years_for_tax * 8)
        print(f'A {type_car} car will pay {total_tax_heavyDuty:.2f} euros in taxes.')
    elif type_car == 'sports':
        kilometres_to_charge = (kilometres // 2000) * 18
        total_tax_sports = kilometres_to_charge + (sports_tax - years_for_tax * 9)
        print(f'A {type_car} car will pay {total_tax_sports:.2f} euros in taxes.')

    total_tax += total_tax_family
    total_tax += total_tax_heavyDuty
    total_tax += total_tax_sports

    total_tax_family = 0
    total_tax_heavyDuty = 0
    total_tax_sports = 0

print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")
