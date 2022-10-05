def round_func(number):
    num_lst = []
    for num in number:
        num_lst.append(round(num))
    return num_lst


numbers = [float(x) for x in input().split()]
print(round_func(numbers))
