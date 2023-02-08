from collections import deque

list_of_the_customers = deque([int(x) for x in input().split(', ')])
list_of_taxis = deque([int(x) for x in input().split(', ')])

total_time = 0

while list_of_the_customers and list_of_taxis:
    current_customer = list_of_the_customers.popleft()
    current_taxi = list_of_taxis.pop()

    if current_taxi >= current_customer:
        total_time += current_customer
    else:
        list_of_the_customers.appendleft(current_customer)

if list_of_the_customers:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(map(str, list_of_the_customers))}')
else:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')