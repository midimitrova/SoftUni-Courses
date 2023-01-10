n = int(input())

even_set = set()
odd_set = set()

for row in range(1, n + 1):
    name_sum = sum([ord(x) for x in input()]) // row
    if name_sum % 2 == 0:
        even_set.add(name_sum)
    else:
        odd_set.add(name_sum)

if sum(even_set) == sum(odd_set):
    current_set = odd_set.union(even_set)
    print(", ".join(map(str, current_set)))
elif sum(odd_set) > sum(even_set):
    current_set = odd_set.difference(even_set)
    print(", ".join(map(str, current_set)))
elif sum(even_set) > sum(odd_set):
    current_set = odd_set.symmetric_difference(even_set)
    print(", ".join(map(str, current_set)))