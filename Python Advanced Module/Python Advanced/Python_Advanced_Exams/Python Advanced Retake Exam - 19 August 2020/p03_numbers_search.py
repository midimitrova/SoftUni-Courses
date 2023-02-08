def numbers_searching(*args):
    duplicates = []
    for number in sorted(args):
        if number not in duplicates:
            count_duplicates = args.count(number)
            if count_duplicates > 1:
                duplicates.append(number)
    full_row = [num for num in range(min(args), max(args) + 1)]
    missing_number = set(full_row) - set(args)
    return [*missing_number, duplicates]


# --- TEST CODE ---
# print(numbers_searching(1, 2, 4, 2, 5, 4))
# print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
# print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))