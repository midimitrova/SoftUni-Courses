type_fuel = input()
littre_fuel = float(input())
club_card = input()

price_gasoline = 2.22
price_diesel = 2.33
price_gas = 0.93

if club_card == "Yes":
    price_gasoline -= 0.18
    price_diesel -= 0.12
    price_gas -= 0.08
    if 20 < littre_fuel <= 25:
        if type_fuel == "Gasoline":
            print(f"{littre_fuel * (price_gasoline - price_gasoline * 8/100):.2f} lv.")
        elif type_fuel == "Diesel":
            print(f"{littre_fuel * (price_diesel - price_diesel * 8/100):.2f} lv.")
        elif type_fuel == "Gas":
            print(f"{littre_fuel * (price_gas - price_gas * 8/100):.2f} lv.")
    elif littre_fuel > 25:
        if type_fuel == "Gasoline":
            print(f"{littre_fuel * (price_gasoline - price_gasoline * 10/100):.2f} lv.")
        elif type_fuel == "Diesel":
            print(f"{littre_fuel * (price_diesel - price_diesel * 10/100):.2f} lv.")
        elif type_fuel == "Gas":
            print(f"{littre_fuel * (price_gas - price_gas * 10/100):.2f} lv.")
    elif littre_fuel < 20:
        if type_fuel == "Gasoline":
            print(f"{littre_fuel * price_gasoline:.2f} lv.")
        elif type_fuel == "Diesel":
            print(f"{littre_fuel * price_diesel:.2f} lv.")
        elif type_fuel == "Gas":
            print(f"{littre_fuel * price_gas:.2f} lv.")

elif club_card == "No":
    if 20 < littre_fuel <= 25:
        if type_fuel == "Gasoline":
            print(f"{littre_fuel * (price_gasoline - price_gasoline * 8 / 100):.2f} lv.")
        elif type_fuel == "Diesel":
            print(f"{littre_fuel * (price_diesel - price_diesel * 8 / 100):.2f} lv.")
        elif type_fuel == "Gas":
            print(f"{littre_fuel * (price_gas - price_gas * 8 / 100):.2f} lv.")
    elif littre_fuel > 25:
        if type_fuel == "Gasoline":
            print(f"{littre_fuel * (price_gasoline - price_gasoline * 0.1):.2f} lv.")
        elif type_fuel == "Diesel":
            print(f"{littre_fuel * (price_diesel - price_diesel * 0.1):.2f} lv.")
        elif type_fuel == "Gas":
            print(f"{littre_fuel * (price_gas - price_gas * 0.1):.2f} lv.")
    elif littre_fuel < 20:
        if type_fuel == "Gasoline":
            print(f"{littre_fuel * price_gasoline:.2f} lv.")
        elif type_fuel == "Diesel":
            print(f"{littre_fuel * price_diesel:.2f} lv.")
        elif type_fuel == "Gas":
            print(f"{littre_fuel * price_gas:.2f} lv.")
