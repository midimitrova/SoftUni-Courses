from collections import deque


def list_manipulator(numbers, *args):
    numbers_list = deque(numbers)

    first_command = args[0]
    second_command = args[1]
    new_numbers = list(args[2:])

    if first_command == 'add' and second_command == 'beginning':
        numbers_list.extendleft(new_numbers[::-1])
        return list(numbers_list)
    elif first_command == 'add' and second_command == 'end':
        numbers_list.extend(new_numbers)
        return list(numbers_list)
    elif first_command == 'remove' and second_command == 'beginning':
        if new_numbers:
            range_num = new_numbers[0]
            for _ in range(range_num):
                numbers_list.popleft()
        else:
            numbers_list.popleft()
        return list(numbers_list)
    elif first_command == 'remove' and second_command == 'end':
        if new_numbers:
            range_num = new_numbers[0]
            for _ in range(range_num):
                numbers_list.pop()
        else:
            numbers_list.pop()
        return list(numbers_list)



# --- TEST CODE---
# print(list_manipulator([1, 2, 3], "remove", "end"))
# print(list_manipulator([1, 2, 3], "remove", "beginning"))
# print(list_manipulator([1, 2, 3], "add", "beginning", 20))
# print(list_manipulator([1, 2, 3], "add", "end", 30))
# print(list_manipulator([1, 2, 3], "remove", "end", 2))
# print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
# print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
# print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
