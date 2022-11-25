tickets = input().replace(" ", "")
tickets = tickets.split(',')
count = 0
symb = ''


def check_next(symbol, first, second):
    back = 6
    for i in range(7, 11):
        if (i * symbol) in first and (i * symbol) in second:
            back += 1
    return back


for ticket in tickets:
    if len(ticket) != 20:
        print('invalid ticket')
        continue
    left = ticket[:int(len(ticket) / 2)]
    right = ticket[int(len(ticket) / 2):]
    if (6 * '@') in left and (6 * '@') in right:
        count = check_next('@', left, right)
        symb = '@'
    elif (6 * '$') in left and (6 * '$') in right:
        count = check_next('$', left, right)
        symb = '$'
    elif (6 * '#') in left and (6 * '#') in right:
        count = check_next('#', left, right)
        symb = '#'
    elif (6 * '^') in left and (6 * '^') in right:
        count = check_next('^', left, right)
        symb = '^'
    else:
        print(f'ticket "{ticket}" - no match')
        continue

    if count != 10:
        print(f'ticket "{ticket}" - {count}{symb}')
    else:
        print(f'ticket "{ticket}" - {count}{symb} Jackpot!')