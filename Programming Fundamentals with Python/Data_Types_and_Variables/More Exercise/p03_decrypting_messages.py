key = int(input())

number_lines = int(input())

message = []

while number_lines > 0:

    letter = input()

    new_letter = chr(ord(letter) + key)

    message.append(new_letter)

    number_lines -= 1

print(''.join(message))