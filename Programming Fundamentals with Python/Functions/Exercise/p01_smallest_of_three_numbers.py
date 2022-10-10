def the_smallest_number(numbers):
    min_num = min(numbers)
    return min_num


first_number = int(input())
second_number = int(input())
third_number = int(input())
number_list = [first_number, second_number, third_number]
print(the_smallest_number(number_list))
