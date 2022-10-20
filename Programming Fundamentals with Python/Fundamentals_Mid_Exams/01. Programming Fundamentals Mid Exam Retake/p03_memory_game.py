elements = [el for el in input().split()]

moves = 0
command = input()
won_game = False

while command != 'end':
    command = command.split()
    first_index = int(command[0])
    second_index = int(command[1])
    moves += 1

    if 0 <= first_index < len(elements) and 0 <= second_index < len(elements) and first_index != second_index:
        if elements[first_index] == elements[second_index]:
            popped_item = elements.pop(first_index)
            elements.remove(popped_item)
            print(f"Congrats! You have found matching elements - {popped_item}!")
        else:
            print("Try again!")
    else:
        middle_elements = len(elements) // 2
        element_to_insert = '-' + str(moves) + 'a'
        elements.insert(middle_elements, element_to_insert)
        elements.insert(middle_elements, element_to_insert)
        print("Invalid input! Adding additional elements to the board")

    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        won_game = True
        break

    command = input()
if not won_game:
    print(f"Sorry you lose :(\n{' '.join(elements)}")
