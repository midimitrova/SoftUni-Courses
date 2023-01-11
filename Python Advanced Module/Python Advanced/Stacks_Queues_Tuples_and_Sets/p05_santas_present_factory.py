from collections import deque

values_of_materials_as_stack = [int(x) for x in input().split()]
magic_values_as_deque = deque([int(x) for x in input().split()])

presents = {'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0}
DOLL = 150
TRAIN = 250
BEAR = 300
BICYCLE = 400

while values_of_materials_as_stack and magic_values_as_deque:

    current_material = values_of_materials_as_stack.pop()
    current_magic_value = magic_values_as_deque.popleft()

    result = current_material * current_magic_value

    if result in [150, 250, 300, 400]:
        if result == DOLL:
            presents['Doll'] += 1
        elif result == TRAIN:
            presents['Wooden train'] += 1
        elif result == BEAR:
            presents['Teddy bear'] += 1
        elif result == BICYCLE:
            presents['Bicycle'] += 1
    elif result < 0:
        new_result = current_material + current_magic_value
        values_of_materials_as_stack.append(new_result)
    elif result > 0:
        values_of_materials_as_stack.append(current_material + 15)
    else:
        if current_material == 0 and current_magic_value == 0:
            continue

        if current_material == 0:
            magic_values_as_deque.appendleft(current_magic_value)

        else:
            values_of_materials_as_stack.append(current_material)

for present, value in presents.items():
    if (presents['Doll'] >= 1 and presents['Wooden train'] >= 1) or \
            (presents['Teddy bear'] >= 1 and presents['Bicycle'] >= 1):
        print('The presents are crafted! Merry Christmas!')
        break
    else:
        print('No presents this Christmas!')
        break

if values_of_materials_as_stack:
    print(f'Materials left: {", ".join(map(str, reversed(values_of_materials_as_stack)))}')

if magic_values_as_deque:
    print(f'Magic left: {", ".join(map(str, magic_values_as_deque))}')

sorted_presents = sorted(presents.items(), key=lambda x: x[0])
for present, value in sorted_presents:
    if value > 0:
        print(f'{present}: {value}')
