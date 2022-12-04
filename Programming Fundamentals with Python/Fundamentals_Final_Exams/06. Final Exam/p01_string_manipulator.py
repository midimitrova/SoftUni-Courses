message = input()

while True:
    command = input().split()

    if command[0] == 'End':
        break

    elif command[0] == 'Translate':
        char = command[1]
        replacement = command[2]
        if char in message:
            message = message.replace(char, replacement)
        print(message)
    elif command[0] == 'Includes':
        substring = command[1]
        if substring in message:
            print('True')
        else:
            print('False')
    elif command[0] == 'Start':
        substring = command[1]
        x = message.startswith(substring)
        print(x)
    elif command[0] == 'Lowercase':
        message = message.lower()
        print(message)
    elif command[0] == 'FindIndex':
        char = command[1]
        x = message.rfind(char)
        print(x)
    elif command[0] == 'Remove':
        start_index = int(command[1])
        count = int(command[2])
        end_index = start_index + count
        message = message[:start_index] + message[end_index:]
        print(message)
