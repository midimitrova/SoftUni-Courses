from collections import deque

bowls_of_ramen_as_stack = [int(x) for x in input().split(', ')]
customers_as_deque = deque([int(x) for x in input().split(', ')])

while bowls_of_ramen_as_stack and customers_as_deque:
    current_bowl = bowls_of_ramen_as_stack.pop()
    current_customer = customers_as_deque.popleft()

    if current_bowl == current_customer:
        continue
    elif current_bowl > current_customer:
        bowls_of_ramen_as_stack.append(current_bowl - current_customer)
    elif current_bowl < current_customer:
        customers_as_deque.appendleft(current_customer - current_bowl)

if not customers_as_deque:
    print('Great job! You served all the customers.')
    if bowls_of_ramen_as_stack:
        print(f'Bowls of ramen left: {", ".join(map(str, bowls_of_ramen_as_stack))}')
else:
    print('Out of ramen! You didn\'t manage to serve all customers.')
    print(f'Customers left: {", ".join(map(str, customers_as_deque))}')