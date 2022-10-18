numbers = [int(num) for num in input().split()]

command = input().split()

while command[0] != 'end':
    current_command = command[0]

    if current_command == 'swap':
        index_one = int(command[1])
        index_two = int(command[2])
        numbers[index_one], numbers[index_two] = numbers[index_two], numbers[index_one]
    elif current_command == 'multiply':
        index_one = int(command[1])
        index_two = int(command[2])
        current_index = int(command[1])
        numbers[index_one] = numbers[index_one] * numbers[index_two]
    elif current_command == 'decrease':
        for i in range(len(numbers)):
            numbers[i] = numbers[i] - 1

    command = input().split()

print(', '.join(map(str, numbers)))
