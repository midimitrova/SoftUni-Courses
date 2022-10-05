def calculates(operator, num1, num2):
    if operator == 'multiply':
        return num1 * num2
    elif operator == 'divide':
        return num1 // num2
    elif operator == 'add':
        return num1 + num2
    elif operator == 'subtract':
        return num1 - num2


oper = input()
number_one = int(input())
number_two = int(input())
print(calculates(oper, number_one, number_two))