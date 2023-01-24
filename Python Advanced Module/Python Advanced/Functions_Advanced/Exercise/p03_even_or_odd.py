def even_odd(*args):
    command = args[-1]

    parity = 0 if command == 'even' else 1
    result = [x for x in args[:len(args) - 1] if x % 2 == parity]

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
