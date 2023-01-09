numbers = tuple(float(x) for x in input().split())

num_occurrences = {}

for num in numbers:
    if num not in num_occurrences:
        num_occurrences[num] = 0
    num_occurrences[num] += 1

for num, count in num_occurrences.items():
    print(f'{num} - {count} times')
