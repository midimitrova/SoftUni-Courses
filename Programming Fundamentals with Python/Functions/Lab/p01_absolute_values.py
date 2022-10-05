def abs_value(nums):
    abs_value = []
    for num in nums:
        abs_value.append(abs(num))
    return abs_value


numbers = [float(x) for x in input().split()]
print(abs_value(numbers))
