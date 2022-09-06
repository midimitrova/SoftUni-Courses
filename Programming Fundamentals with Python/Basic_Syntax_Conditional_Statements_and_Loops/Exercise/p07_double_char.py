
command = input()

while command != 'End':

    if command == 'SoftUni':
        command = input()
        continue

    for letter in command:
        double_letter = letter * 2
        print(''.join(double_letter), end='')

    print()
    command = input()