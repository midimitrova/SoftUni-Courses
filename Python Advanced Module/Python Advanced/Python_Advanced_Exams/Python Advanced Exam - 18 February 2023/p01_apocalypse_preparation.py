from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = deque([int(x) for x in input().split()])

healing_items = {
    'Patch': [30, 0],
    'Bandage': [40, 0],
    'MedKit': [100, 0],
}

while textiles and medicaments:

    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()

    current_sum = current_textile + current_medicament

    for item, resource in healing_items.items():

        if current_sum == resource[0]:
            healing_items[item][1] += 1
            break
    else:
        if current_sum > healing_items['MedKit'][0]:
            healing_items['MedKit'][1] += 1
            remaining_resource = current_sum - healing_items['MedKit'][0]
            next_medicament = medicaments.pop()
            medicaments.append(next_medicament + remaining_resource)
        else:
            medicaments.append(current_medicament + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not medicaments:
    print("Medicaments are empty.")
elif not textiles:
    print("Textiles are empty.")

sorted_dict = dict(sorted(healing_items.items(), key=lambda x: (-x[1][1], x[0])))
for item, value in sorted_dict.items():
    if value[1] > 0:
        print(f"{item} - {value[1]}")

if medicaments:
    print(f"Medicaments left: {', '.join(map(str, reversed(medicaments)))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str,textiles))}")
