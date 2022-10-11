def multiplication(num1, num2, num3):
    if num1 > 0 and num2 > 0 and num3 > 0:
        return 'positive'
    elif num1 < 0 or num2 < 0 or num3 < 0:
        if num1 == 0 or num2 == 0 or num3 == 0:
            return 'zero'
        elif num1 > 0 and num2 < 0 and num3 < 0:
            return 'positive'
        elif num1 < 0 and num2 < 0 and num3 > 0:
            return 'positive'
        elif num1 < 0 and num2 > 0 and num3 < 0:
            return 'positive'
        return 'negative'
    elif num1 == 0 or num2 == 0 or num3 == 0:
        return 'zero'


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(multiplication(first_number, second_number, third_number))
