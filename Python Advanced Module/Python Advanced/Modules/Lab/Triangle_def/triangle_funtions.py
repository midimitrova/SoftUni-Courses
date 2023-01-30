def upper_part(num):
    for number_one in range(1, num + 1):
        for number_two in range(1, number_one + 1):
            print(number_two, end=' ')
        print()


def down_part(num):
    for number_one in range(num, 0, -1):
        for number_two in range(1, number_one):
            print(number_two, end=' ')
        print()


def print_triangle(num):
    upper_part(num)
    down_part(num)
