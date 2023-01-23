def operate(symbol, *args):
    result = args[0]

    if symbol == '+':
        for el in args[1:]:
            result += el
    elif symbol == '-':
        for el in args[1:]:
            result -= el
    elif symbol == '/':
        for el in args[1:]:
            result /= el
    elif symbol == '*':
        for el in args[1:]:
            result *= el

    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("-", 17, 12, 3))
print(operate("/", 20, 5, 2))

