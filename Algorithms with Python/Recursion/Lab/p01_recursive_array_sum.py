def array_sum(my_num, index):
    if index >= len(my_num) - 1:
        return my_num[index]
    return my_num[index] + array_sum(my_num, index + 1)

my_num = [int(my_num) for my_num in input().split()]

print(array_sum(my_num, 0))
