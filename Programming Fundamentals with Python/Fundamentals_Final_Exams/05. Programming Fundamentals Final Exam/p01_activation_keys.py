activation_key = input()


while True:
    data = input().split('>>>')
    command = data[0]

    if command == 'Generate':
        print(f'Your activation key is: {activation_key}')
        break
    elif command == 'Contains':
        substring = data[1]
        if substring in activation_key:
            print(f'{activation_key} contains {substring}')
        else:
            print('Substring not found!')
    elif command == 'Flip':
        upper_or_lower = data[1]
        start_index = int(data[2])
        end_index = int(data[3])
        substring_to_change = activation_key[start_index:end_index]
        if upper_or_lower == 'Upper':
            substring_to_change = substring_to_change.upper()
        else:
            substring_to_change = substring_to_change.lower()
        activation_key = activation_key[:start_index] + substring_to_change + activation_key[end_index:]
        print(activation_key)
    elif command == 'Slice':
        start_index = int(data[1])
        end_index = int(data[2])
        substring_to_delete = activation_key[start_index:end_index]
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

