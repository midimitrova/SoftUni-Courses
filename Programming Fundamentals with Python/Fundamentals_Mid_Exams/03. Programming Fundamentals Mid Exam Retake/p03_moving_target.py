targets = [int(num) for num in input().split()]

command = input()
while command != 'End':
    command = command.split()
    current_command = command[0]

    if current_command == 'Shoot':
        index = int(command[1])
        power = int(command[2])

        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif current_command == 'Add':
        index = int(command[1])
        value = int(command[2])

        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif current_command == 'Strike':
        index = int(command[1])
        radius = int(command[2])

        if 0 <= index - radius and index + radius < len(targets):
            targets = [targets[i] for i in range(len(targets)) if i < index - radius or i > index + radius]
        else:
            print("Strike missed!")
    command = input()

print('|'.join(map(str, targets)))
