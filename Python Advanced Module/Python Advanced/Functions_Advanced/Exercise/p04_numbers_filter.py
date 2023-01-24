def even_odd_filter(**kwargs):
    new_dict = {}
    for command, values in kwargs.items():
        parity = 0 if command == 'even' else 1
        result = [x for x in values if x % 2 == parity]

        new_dict[command] = result
    sorted_dict = dict(sorted(new_dict.items(), key=lambda x: -len(x[1])))

    return sorted_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
