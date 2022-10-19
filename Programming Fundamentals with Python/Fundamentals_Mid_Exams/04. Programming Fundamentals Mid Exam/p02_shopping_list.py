groceries = input().split('!')

command = input()
while command != 'Go Shopping!':
    command = command.split()
    current_command = command[0]

    if current_command == 'Urgent':
        item = command[1]
        if item not in groceries:
            groceries.insert(0, item)
    elif current_command == 'Unnecessary':
        item = command[1]
        if item in groceries:
            groceries.remove(item)
    elif current_command == 'Correct':
        old_item = command[1]
        new_item = command[2]
        if old_item in groceries:
            index = groceries.index(old_item)
            groceries.remove(old_item)
            groceries.insert(index, new_item)
    elif current_command == 'Rearrange':
        item = command[1]
        if item in groceries:
            groceries.append(item)
            groceries.remove(item)
    command = input()

print(', '.join(groceries))
