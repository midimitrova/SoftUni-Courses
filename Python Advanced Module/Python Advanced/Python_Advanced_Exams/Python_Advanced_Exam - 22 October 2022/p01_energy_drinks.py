from collections import deque

max_caffeine = 300
result = 0
current_caffeine = 0

milligrams_of_caffeine_stack = [int(x) for x in input().split(', ')]
energy_drinks_deque = deque([int(x) for x in input().split(', ')])

while milligrams_of_caffeine_stack and energy_drinks_deque and max_caffeine > 0:
    current_milligram_caffeine = milligrams_of_caffeine_stack.pop()
    current_energy_drink = energy_drinks_deque.popleft()

    result = current_milligram_caffeine * current_energy_drink

    if max_caffeine >= result:
        max_caffeine -= result
        current_caffeine += result
    elif max_caffeine < result:
        energy_drinks_deque.append(current_energy_drink)
        current_caffeine -= 30
        if current_caffeine < 0:
            current_caffeine = 0
        else:
            max_caffeine += 30

if energy_drinks_deque:
    print(f'Drinks left: {", ".join(map(str, energy_drinks_deque))}')
else:
    print('At least Stamat wasn\'t exceeding the maximum caffeine.')
print(f'Stamat is going to sleep with {current_caffeine} mg caffeine.')
