first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

n_lines = int(input())
ADD_FIRST = 'Add First'
ADD_SECOND = 'Add Second'
REMOVE_FIRST = 'Remove First'
REMOVE_SECOND = 'Remove Second'
CHECK_SUBSET = 'Check Subset'

for _ in range(n_lines):
    command = input().split()
    current_command = f'{command[0]} {command[1]}'
    current_set = set(int(x) for x in command[2:])
    if current_command == ADD_FIRST:
        first_set = first_set.union(current_set)
    elif current_command == ADD_SECOND:
        second_set = second_set.union(current_set)
    elif current_command == REMOVE_FIRST:
        first_set = first_set.difference(current_set)
    elif current_command == REMOVE_SECOND:
        second_set = second_set.difference(current_set)
    elif current_command == CHECK_SUBSET:
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print('True')
        else:
            print('False')

print(f"{', '.join(map(str, sorted(first_set)))}")
print(f"{', '.join(map(str, sorted(second_set)))}")
