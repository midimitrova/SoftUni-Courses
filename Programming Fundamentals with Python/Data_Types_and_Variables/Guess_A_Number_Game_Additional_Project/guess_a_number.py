import random

computer_number = random.randint(1, 100)

while True:
    user_number = input('Guess a number in range(1, 100) ')

    if not user_number.isdigit():
        print('Invalid input! Please, enter a number in range(1, 100) ')
        continue

    user_number = int(user_number)

    if user_number > computer_number:
        print('Too High! Try again.')
    elif user_number < computer_number:
        print('Too Low! Try again.')
    else:
        print('You guess it!')
        break