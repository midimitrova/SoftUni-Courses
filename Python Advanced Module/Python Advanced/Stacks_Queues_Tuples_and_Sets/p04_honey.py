from collections import deque

working_bees_as_deque = deque([int(x) for x in input().split()])
nectar_as_stack = [int(x) for x in input().split()]
symbols_as_deque = deque(input().split())

collected_nectar = deque()
total_nectar = 0

while working_bees_as_deque and nectar_as_stack:
    bee = working_bees_as_deque[0]
    nectar = nectar_as_stack.pop()

    if bee > nectar:
        continue
    elif bee <= nectar:
        collected_nectar.append(working_bees_as_deque.popleft())
        collected_nectar.append(nectar)
        operator = symbols_as_deque.popleft()
        if operator == '/' and nectar == 0:
            continue
        else:
            result = abs(eval(f'{collected_nectar.popleft()} {operator} {collected_nectar.popleft()}'))
        total_nectar += result


print(f'Total honey made: {total_nectar}')
if working_bees_as_deque:
    print(f'Bees left: {", ".join(map(str, working_bees_as_deque))}')
if nectar_as_stack:
    print(f'Nectar left: {", ".join(map(str, nectar_as_stack))}')

