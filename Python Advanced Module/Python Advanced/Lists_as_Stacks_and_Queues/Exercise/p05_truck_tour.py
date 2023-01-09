from collections import deque

petrol_pumps = int(input())
pumps = deque()

for _ in range(petrol_pumps):
    pump_data = [int(x) for x in input().split()]
    pumps.append(pump_data)

for attempt in range(petrol_pumps):
    tank_quantity = 0
    failed = False
    for fuel, distance in pumps:
        tank_quantity += fuel

        if distance > tank_quantity:
            failed = True
            break
        else:
            tank_quantity -= distance

    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break
