numbers = [int(x) for x in input().split()]


def even_numbers(nums):
    return nums % 2 == 0


even_filter = filter(even_numbers, numbers)
even_lst = list(even_filter)
print(even_lst)
