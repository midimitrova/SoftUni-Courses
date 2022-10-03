numbers = input().split()

sequence_of_numbers = []
for num in numbers:
    sequence_of_numbers.append(int(num))

command = input().split()
while command[0] != 'end':
    even_num = []
    odd_num = []
    for num in sequence_of_numbers:
        if num % 2 == 0:
            even_num.append(num)
        else:
            odd_num.append(num)

    if command[0] == 'exchange':
        if 0 <= int(command[1]) < len(sequence_of_numbers):
            sequence_of_numbers = sequence_of_numbers[int(command[1]) + 1:] \
                                  + sequence_of_numbers[:int(command[1]) + 1]
        else:
            print("Invalid index")

    elif command[0] == "max":
        if command[1] == "even" and even_num:
            print((len(sequence_of_numbers) - sequence_of_numbers[::-1].index(max(even_num)) - 1))
        elif command[1] == "odd" and odd_num:
            print((len(sequence_of_numbers) - sequence_of_numbers[::-1].index(max(odd_num)) - 1))
        else:
            print('No matches')

    elif command[0] == "min":
        if command[1] == "even" and even_num:
            print((len(sequence_of_numbers) - sequence_of_numbers[::-1].index(min(even_num)) - 1))
        elif command[1] == "odd" and odd_num:
            print((len(sequence_of_numbers) - sequence_of_numbers[::-1].index(min(odd_num)) - 1))
        else:
            print('No matches')

    elif command[0] == "first":
        if 0 < int(command[1]) <= len(sequence_of_numbers):
            if command[2] == "even":
                print(even_num[0:int(command[1])])
            else:
                print(odd_num[0:int(command[1])])
        else:
            print(f"Invalid count")

    elif command[0] == "last":
        if 0 < int(command[1]) <= len(sequence_of_numbers):
            if command[2] == "even":
                print(even_num[-int(command[1]):])
            else:
                print(odd_num[-int(command[1]):])
        else:
            print(f"Invalid count")

    command = input().split()

print(sequence_of_numbers)
