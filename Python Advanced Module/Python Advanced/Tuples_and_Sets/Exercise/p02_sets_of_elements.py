n, m = [int(x) for x in input().split()]

first_set = set()
second_set = set()

for _ in range(n):
    num = int(input())
    first_set.add(num)

for _ in range(m):
    num = int(input())
    second_set.add(num)

unique_elements = first_set.intersection(second_set)
print('\n'.join(map(str, unique_elements)))