from collections import deque

materials = deque([int(x) for x in input().split()])
magic = deque([int(x) for x in input().split()])

catalogue = {
    'Gemstone': [100, 199], 'Porcelain Sculpture': [200, 299],
    'Gold': [300, 399], 'Diamond Jewellery': [400, 499]}

created_presents = {
    'Gemstone': 0, 'Porcelain Sculpture': 0,
    'Gold': 0, 'Diamond Jewellery': 0}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()

    product = current_material + current_magic

    if product < 100:
        if product % 2 == 0:
            product = current_material * 2 + current_magic * 3
        else:
            product *= 2
    elif product > 499:
        product /= 2

    if 100 <= product <= 499:
        for gift, cost in catalogue.items():
            if cost[0] <= product <= cost[1]:
                created_presents[gift] += 1
                break

success = created_presents['Gemstone'] > 0 and created_presents['Porcelain Sculpture'] > 0 or \
          created_presents['Gold'] > 0 and created_presents['Diamond Jewellery'] > 0

if success:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f'Materials left: {", ".join(map(str, materials))}')
if magic:
    print(f'Magic left: {", ".join(map(str, magic))}')

sorted_dict = sorted(created_presents.items(), key=lambda x: x[0])
for present, value in sorted_dict:
    if value >= 1:
        print(f'{present}: {value}')