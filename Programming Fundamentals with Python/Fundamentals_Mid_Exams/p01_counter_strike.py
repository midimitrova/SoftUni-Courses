initial_energy = int(input())

won_battles = 0

command = input()
while command != "End of battle":
    distance_of_an_enemy = int(command)
    if initial_energy > 0 and initial_energy >= distance_of_an_enemy:
        initial_energy -= distance_of_an_enemy
        won_battles += 1
        if won_battles % 3 == 0:
            initial_energy += won_battles
    else:
        break
    command = input()

if (initial_energy > 0 and initial_energy >= distance_of_an_enemy) or command == "End of battle":
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}")
else:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")

