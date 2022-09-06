n = int(input())

while n > 0:
    number = int(input())

    if number == 88:
        print('Hello')
    elif number == 86:
        print('How are you?')
    elif 88 > number and number != 88 and number != 86:
        print('GREAT!')
    elif number > 88:
        print('Bye.')

    n -= 1