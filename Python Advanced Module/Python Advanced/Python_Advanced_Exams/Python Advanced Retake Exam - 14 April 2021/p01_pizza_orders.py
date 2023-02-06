from collections import deque

pizza_orders = deque([int(x) for x in input().split(', ')])
employee_capacity = deque([int(x) for x in input().split(', ')])

total_pizza = 0

while pizza_orders and employee_capacity:
    current_pizza_order = pizza_orders.popleft()
    current_employee = employee_capacity.pop()

    if current_pizza_order <= 0:
        employee_capacity.append(current_employee)
        continue
    if current_pizza_order > 10:
        employee_capacity.append(current_employee)
        continue
    if current_pizza_order <= current_employee:
        total_pizza += current_pizza_order
    elif current_pizza_order > current_employee:
        left_pizza = current_pizza_order - current_employee
        pizza_orders.appendleft(left_pizza)
        total_pizza += current_employee

if not pizza_orders:
    print(f'All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizza}')
    print(f'Employees: {", ".join(map(str, employee_capacity))}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(map(str, pizza_orders))}')