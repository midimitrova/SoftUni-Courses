def sum_numbers(num1, num2):
    total = num1 + num2
    return total


def subtract(sum, num3):
    result = sum - num3
    return result


def add_and_subtract(num1, num2, num3):
    sum_first_two = sum_numbers(num1, num2)
    final_result = subtract(sum_first_two, num3)
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number,second_number,third_number))
