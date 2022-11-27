numbers = input().split()

decrypted_msg = []
current_msg = ''

data = input()
while data != 'find':
    i_numbers = 0
    for i_letters in range(len(data)):
        current_letter = ord(data[i_letters])
        current_letter -= int(numbers[i_numbers])
        current_msg += chr(current_letter)
        i_numbers += 1
        if i_numbers == len(numbers):
            i_numbers = 0

    decrypted_msg.append(current_msg)
    current_msg = ''

    data = input()

for message in decrypted_msg:
    treasure = []
    coordinates = []
    for index_letter in range(len(message)):
        if message[index_letter] == '&':
            index_letter += 1
            while message[index_letter] != '&':
                treasure.append(message[index_letter])
                index_letter += 1
            break

    for index_coord in range(len(message)):
        if message[index_coord] == '<':
            index_coord += 1
            while message[index_coord] != '>':
                coordinates.append(message[index_coord])
                index_coord += 1

    print(f"Found {''.join(treasure)} at {''.join(coordinates)}")
