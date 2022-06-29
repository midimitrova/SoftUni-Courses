number_bottles = int(input())

left_quantity_preparation = number_bottles * 750
dish_preparation_quantity = 5
pot_preparation_quantity = 15
charging = 0
number_dishes = 0
number_pots = 0

command = input()
while command != "End":
    curr_command = int(command)

    charging += 1

    if charging % 3 == 0:
        left_quantity_preparation -= (curr_command * pot_preparation_quantity)
        number_pots += curr_command
    else:
        left_quantity_preparation -= (curr_command * dish_preparation_quantity)
        number_dishes += curr_command

    if left_quantity_preparation < 0:
        break

    command = input()

if command == "End":
    print("Detergent was enough!")
    print(f"{number_dishes} dishes and {number_pots} pots were washed.")
    print(f"Leftover detergent {left_quantity_preparation} ml.")

elif left_quantity_preparation < 0:
    print(f"Not enough detergent, {abs(left_quantity_preparation)} ml. more necessary!")
