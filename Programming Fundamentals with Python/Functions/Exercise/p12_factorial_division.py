def factorial_division(number):
    factorial = 1
    for num in range(1, number + 1):
        factorial *= num
    return factorial


first_number = int(input())
second_number = int(input())
first_factorial = factorial_division(first_number)
second_factorial = factorial_division(second_number)
division = first_factorial / second_factorial
print(f'{division:.2f}')