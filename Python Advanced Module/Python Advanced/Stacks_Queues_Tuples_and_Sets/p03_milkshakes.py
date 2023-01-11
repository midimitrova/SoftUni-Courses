from collections import deque

chocolates_as_stack = [int(x) for x in input().split(', ')]
cups_of_milk_as_deque = deque([int(x) for x in input().split(', ')])

ready_milkshakes = 0

while chocolates_as_stack and cups_of_milk_as_deque and ready_milkshakes < 5:
    current_chocolate = chocolates_as_stack.pop()
    current_cup = cups_of_milk_as_deque.popleft()

    if current_chocolate <= 0 and current_cup <= 0:
        continue

    if current_cup <= 0:
        chocolates_as_stack.append(current_chocolate)
        continue

    if current_chocolate <= 0:
        cups_of_milk_as_deque.appendleft(current_cup)
        continue

    if current_chocolate == current_cup:
        ready_milkshakes += 1
    else:
        cups_of_milk_as_deque.append(current_cup)
        chocolates_as_stack.append(current_chocolate - 5)


if ready_milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolates_as_stack:
    print(f'Chocolate: {", ".join(map(str, chocolates_as_stack))}')
else:
    print('Chocolate: empty')

if cups_of_milk_as_deque:
    print(f'Milk: {", ".join(map(str, cups_of_milk_as_deque))}')
else:
    print('Milk: empty')
