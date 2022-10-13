number = int(input())
wagons = [0] * number
command = input().split()

while True:

    if command[0] == 'End':
        break

    current_command = command[0]

    if current_command == 'add':
        add_people = int(command[1])
        wagons[-1] += add_people
    elif current_command == 'insert':
        index = int(command[1])
        insert_people = int(command[2])
        wagons[index] += insert_people
    elif current_command == 'leave':
        index = int(command[1])
        leave_people = int(command[2])
        wagons[index] -= leave_people
    command = input().split()

print(wagons)