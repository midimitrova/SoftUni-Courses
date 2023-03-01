from itertools import permutations


def possible_permutations(numbers):
    for per in permutations(numbers):
        yield list(per)


# --- test code ---
# [print(n) for n in possible_permutations([1, 2, 3])]
#
# [print(n) for n in possible_permutations([1])]
