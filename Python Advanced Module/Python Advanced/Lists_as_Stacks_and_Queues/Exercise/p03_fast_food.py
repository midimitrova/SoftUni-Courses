from collections import deque

quantity_of_food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

enough_quantity = True

while orders:
    current_order = orders[0]
    if quantity_of_food >= current_order:
        quantity_of_food -= current_order
        orders.popleft()
    else:
        enough_quantity = False
        break

if enough_quantity:
    print('Orders complete')
else:
    print(f'Orders left: {" ".join(map(str, orders))}')
