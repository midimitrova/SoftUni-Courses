text = input()

parenthesis = []
is_balanced = True
for symbol in text:
    if symbol in ['{', '[', '(']:
        parenthesis.append(symbol)
    elif not parenthesis:
        is_balanced = False
        break
    else:
        last_opening_bracket = parenthesis.pop()
        if f'{last_opening_bracket}{symbol}' not in ['()', '[]', '{}']:
            is_balanced = False
            break

if is_balanced:
    print('YES')
else:
    print('NO')
