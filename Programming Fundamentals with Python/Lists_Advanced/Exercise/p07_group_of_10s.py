numbers_list = [int(num) for num in input().split(', ')]

max_number = max(numbers_list)
max_group = max_number
number = 0
lst = []

while max_group % 10 != 0:
    max_group += 1

while number != max_group:
    number += 10
    for i in numbers_list:
        if int(i) <= number:
            lst.append(i)
    print(f"Group of {number}'s: {lst}")
    for i in lst:
        numbers_list.remove(i)
    lst.clear()

