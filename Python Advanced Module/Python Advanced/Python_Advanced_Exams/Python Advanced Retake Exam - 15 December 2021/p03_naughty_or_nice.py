def naughty_or_nice_list(*args, **kwargs):
    santa_claus_data = {
        'Nice': [],
        'Naughty': [],
        'Not found': [],
    }

    santa_list, commands = args[0], args[1:]
    santa_list_copy = santa_list.copy()
    for command in commands:
        num, type_child = command.split('-')
        num = int(num)

        count = 0
        child = []
        correct_num = 0

        for children_data in santa_list_copy:
            if children_data[0] == num:
                count += 1
                child.append(children_data[1])
                correct_num = num

        if count == 1:
            santa_claus_data[type_child].extend(child)
            for child_data in santa_list:
                if child_data[1] in child and correct_num == child_data[0]:
                    santa_list.remove(child_data)

    for command_kwrags in kwargs.items():
        name = command_kwrags[0]
        child_type = command_kwrags[1]
        count = 0
        child = []

        for children_data in santa_list:
            if name == children_data[1]:
                count += 1
                child.append(children_data[1])

        if count == 1:
            santa_claus_data[child_type].extend(child)
            for child_data in santa_list:
                if child_data[1] in child:
                    santa_list.remove(child_data)

    if santa_list_copy:
        for child in santa_list:
            santa_claus_data['Not found'].append(child[1])

    output = ''
    for child_type, name in santa_claus_data.items():
        if name:
            output += f'{child_type}: {", ".join(name)}\n'

    return output

# --- TEST CODE ---
# print(naughty_or_nice_list(
#     [
#         (3, "Amy"),
#         (1, "Tom"),
#         (7, "George"),
#         (3, "Katy"),
#     ],
#     "3-Nice",
#     "1-Naughty",
#     Amy="Nice",
#     Katy="Naughty",
# ))
#
# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
# ))
#
# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))
