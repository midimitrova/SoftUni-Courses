import random

points_user = 0
points_computer = 0

while True:
    computer_option = random.choice(['rock', 'paper', 'scissors'])
    user_input = input('Please, choose one of: rock, paper or scissors: ')

    if user_input not in ['rock', 'paper', 'scissors']:
        print('Invalid input! Please, enter one of: rock, paper or scissors:  ')
        continue

    if (user_input == 'rock' and computer_option == 'scissors') or\
        (user_input == 'paper' and computer_option == 'rock') or\
        (user_input == 'scissors' and computer_option == 'paper'):
        points_user += 1
        print('You win!')
    elif user_input == computer_option:
        print('Draw!')
    else:
        points_computer += 1
        print('You lose!')

    if points_user == 5 or points_computer == 5:
        if points_user == 5:
            print('You win the game!')
            break
        else:
            print('You lost the game!')
            break
