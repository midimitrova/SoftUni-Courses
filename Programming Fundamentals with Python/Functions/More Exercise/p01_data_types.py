def myFunc(current_command, new_str):
    if current_command == 'int':
        return int(new_str) * 2
    elif current_command == 'real':
        return f'{(float(new_str) * 1.5):.2f}'
    elif current_command == 'string':
        return f'${new_str}$'


command = input()
current_str = input()
print(myFunc(command, current_str))
