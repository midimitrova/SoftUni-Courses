from simple_operations.helper import operations_dictionary


text = input().split()

a = float(text[0])
symbol = text[1]
b = float(text[2])

try:
    print(f'{operations_dictionary[symbol](a, b):.2f}')
except ZeroDivisionError:
    print('You cannot divide by zero!')
