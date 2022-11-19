encrypted_message = input()

command = input().split('|')
while command[0] != 'Decode':

    if command[0] == 'Move':
        number_of_letters = int(command[1])
        for _ in range(number_of_letters):
            encrypted_message = encrypted_message[1:] + encrypted_message[0]
    elif command[0] == 'Insert':
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        while substring in encrypted_message:
            encrypted_message = encrypted_message.replace(substring, replacement)
    command = input().split('|')

print(f'The decrypted message is: {encrypted_message}')
