numbers = [int(num) for num in input().split()]

greater_nums = []
average_num = sum(numbers) // len(numbers)

for num in numbers:
    if num > average_num:
        greater_nums.append(num)

if len(greater_nums) == 0:
    print("No")

sorted_numbers = sorted(greater_nums, reverse=True)
sorted_numbers = sorted_numbers[:5]

print(' '.join(map(str, sorted_numbers)))
