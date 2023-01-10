n = int(input())

unique_elements = set()

for _ in range(n):
    element = input().split()
    unique_elements = unique_elements.union(element)

print('\n'.join(unique_elements))