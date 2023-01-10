def gen_seq(range_info):
    star, end = [int(x) for x in range_info.split(',')]
    return set(range(star, end + 1))


n = int(input())

max_range = 0
longest_intersection = set()

for _ in range(n):
    nums_ranges = input().split('-')
    first_set = gen_seq(nums_ranges[0])
    second_set = gen_seq(nums_ranges[1])
    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > max_range:
        max_range = len(current_intersection)
        longest_intersection = current_intersection

print(f'Longest intersection is [{", ".join(map(str, longest_intersection))}] with length {max_range}')
