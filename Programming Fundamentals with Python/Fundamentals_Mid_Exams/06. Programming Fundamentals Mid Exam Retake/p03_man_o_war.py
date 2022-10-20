pirate_ship = [int(num) for num in input().split(">")]
warship = [int(num) for num in input().split(">")]
max_health_capacity = int(input())

command = input()
is_sunk = False
while command != 'Retire':
    command = command.split()
    current_command = command[0]

    if current_command == 'Fire':
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                is_sunk = True
                break
    elif current_command == 'Defend':
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])

        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for index in range(start_index, end_index + 1):
                pirate_ship[index] -= damage
                if pirate_ship[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_sunk = True
                    break
    elif current_command == 'Repair':
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health_capacity:
                pirate_ship[index] = max_health_capacity
    elif current_command == 'Status':
        need_repair_status = max_health_capacity * 0.2
        need_repair_count = 0
        for index in range(len(pirate_ship)):
            if pirate_ship[index] < need_repair_status:
                need_repair_count += 1
        print(f"{need_repair_count} sections need repair.")

    command = input()

if not is_sunk:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
