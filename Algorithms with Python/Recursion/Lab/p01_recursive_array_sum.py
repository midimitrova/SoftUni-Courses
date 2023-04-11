def sum_numbers(numbers, num_idx):
    if num_idx == len(numbers) - 1:
        return numbers[num_idx]

    return numbers[num_idx] + sum_numbers(numbers, num_idx + 1)


nums = [int(x) for x in input().split()]
print(sum_numbers(nums, 0))
