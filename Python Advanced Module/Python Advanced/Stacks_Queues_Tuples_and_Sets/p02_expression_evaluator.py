from math import floor
from collections import deque

current_symbols = deque()
current_result = 0
expression = deque(input().split())

for symbol_index in range(len(expression)):
    symbol = expression[symbol_index]
    if symbol.isdigit():
        current_symbols.append(int(symbol))
    elif len(symbol) > 1:
        if symbol.lstrip('-').replace('-', '', 1).isdigit():
            current_symbols.append(int(symbol))
    else:
        while len(current_symbols) > 1:
            current_result = eval(f'{current_symbols.popleft()} {symbol} {current_symbols.popleft()}')
            current_symbols.appendleft(floor(current_result))

print(*current_symbols)
