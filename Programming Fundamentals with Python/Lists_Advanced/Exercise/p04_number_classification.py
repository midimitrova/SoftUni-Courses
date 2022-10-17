def positive(numbers):
    positive_nums = []
    for num in numbers:
        if num >= 0:
            positive_nums.append(str(num))
    return ', '.join(positive_nums)


def negative(numbers):
    negative_nums = []
    for num in numbers:
        if num < 0:
            negative_nums.append(str(num))
    return ', '.join(negative_nums)


def even(numbers):
    even_nums = []
    for num in numbers:
        if num % 2 == 0:
            even_nums.append(str(num))
    return ', '.join(even_nums)


def odd(numbers):
    odd_nums = []
    for num in numbers:
        if num % 2 != 0:
            odd_nums.append(str(num))
    return ', '.join(odd_nums)


int_numbers = [int(num) for num in input().split(', ')]
print(f'Positive: {positive(int_numbers)}')
print(f'Negative: {negative(int_numbers)}')
print(f'Even: {even(int_numbers)}')
print(f'Odd: {odd(int_numbers)}')
