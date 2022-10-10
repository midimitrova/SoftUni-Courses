def min_num(num):
    return min(num)


def max_num(num):
    return max(num)


def sum_num(num):
    return sum(num)


numbers = [int(x) for x in input().split()]
print(f"The minimum number is {min_num(numbers)}")
print(f"The maximum number is {max_num(numbers)}")
print(f"The sum number is: {sum_num(numbers)}")
