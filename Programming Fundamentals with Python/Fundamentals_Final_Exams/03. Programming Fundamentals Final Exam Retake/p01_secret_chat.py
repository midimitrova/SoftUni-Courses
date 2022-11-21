concealed_message = input()

data = input().split(':|:')

while True:

    command = data[0]

    if command == 'Reveal':
        print(f'You have a new text message: {concealed_message}')
        break
    elif command == 'InsertSpace':
        index = int(data[1])
        concealed_message = concealed_message[:index] + ' ' + concealed_message[index:]
    elif command == 'Reverse':
        substring = data[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, '', 1)
            reversed_substring = substring[::-1]
            concealed_message = concealed_message[::] + reversed_substring
        else:
            print('error')
            data = input().split(':|:')
            continue
    elif command == 'ChangeAll':
        substring = data[1]
        replacement = data[2]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)

    print(concealed_message)

    data = input().split(':|:')
