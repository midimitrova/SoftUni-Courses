items = input().split(', ')

command = input()

while command != 'Craft!':
    splitted_commands = command.split(' - ')
    current_command = splitted_commands[0]

    if current_command == 'Collect':
        item = splitted_commands[1]
        if item not in items:
            items.append(item)
    elif current_command == 'Drop':
        item = splitted_commands[1]
        if item in items:
            items.remove(item)
    elif current_command == 'Combine Items':
        old_item, new_item = splitted_commands[1].split(':')
        if old_item in items:
            index = items.index(old_item)
            items.insert(index + 1, new_item)
    elif current_command == 'Renew':
        item = splitted_commands[1]
        if item in items:
            items.append(item)
            items.remove(item)

    command = input()
print(', '.join(items))
