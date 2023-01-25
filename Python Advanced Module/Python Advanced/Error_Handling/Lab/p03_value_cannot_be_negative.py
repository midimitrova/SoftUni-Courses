class ValueCannotBeNegative(Exception):
    pass


idx = 5
while idx > 0:

    number = int(input())

    if number < 0:
        raise ValueCannotBeNegative

    idx -= 1
