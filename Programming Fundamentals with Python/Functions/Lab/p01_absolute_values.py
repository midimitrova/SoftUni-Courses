def abs_value(nums):
    abs_value_lst = []
    for num in nums:
        abs_value_lst.append(abs(num))
    return abs_value_lst


numbers = [float(x) for x in input().split()]
print(abs_value(numbers))