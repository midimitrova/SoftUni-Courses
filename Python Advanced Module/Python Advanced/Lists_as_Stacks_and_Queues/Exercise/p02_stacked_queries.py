lines = int(input())

query_stack = []

while lines > 0:
    query_data = input().split()
    command = query_data[0]

    if command == '1':
        num_to_add = int(query_data[1])
        query_stack.append(num_to_add)
    elif command == '2' and query_stack:
        query_stack.pop()
    elif command == '3' and query_stack:
        print(max(query_stack))
    elif command == '4' and query_stack:
        print(min(query_stack))

    lines -= 1

while query_stack:
    popped_item = query_stack.pop()
    if query_stack:
        print(popped_item, end=', ')
    else:
        print(popped_item)

