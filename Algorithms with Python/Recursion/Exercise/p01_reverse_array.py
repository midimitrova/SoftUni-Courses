def reverse_numbers(left_idx, numbers):
    if left_idx == len(numbers) // 2:
        print(*numbers, sep=' ')
        return

    right_index = len(numbers) - 1 - left_idx
    numbers[left_idx], numbers[right_index] = numbers[right_index], numbers[left_idx]
    reverse_numbers(left_idx + 1, numbers)


numbers = [int(x) for x in input().split()]

reverse_numbers(0, numbers)
