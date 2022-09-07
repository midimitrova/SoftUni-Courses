command = input()
command_list = []

while command != 'Welcome!':

    command_list.append(command)

    if command == 'Voldemort':
        print("You must not speak of that name!")
        break

    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    elif len(command) > 6:
        print(f"{command} goes to Hufflepuff.")

    command = input()

if 'Voldemort' not in command_list:
    print("Welcome to Hogwarts.")