text = input()

parenthesis = []
for symbol_index in range(len(text)):
    if text[symbol_index] == '(':
        parenthesis.append(symbol_index)
    elif text[symbol_index] == ')':
        start_index = parenthesis.pop()
        print(text[start_index:symbol_index+1])
