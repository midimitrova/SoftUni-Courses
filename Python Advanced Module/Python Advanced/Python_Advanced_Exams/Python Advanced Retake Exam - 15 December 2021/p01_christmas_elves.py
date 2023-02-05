from collections import deque

elf_energy = deque([int(x) for x in input().split()])
number_of_materials_in_box = deque([int(x) for x in input().split()])

total_used_energy = 0
made_toys = 0
taking_box = 0

while elf_energy and number_of_materials_in_box:

    current_elf_energy = elf_energy.popleft()
    current_material = number_of_materials_in_box.pop()

    if current_elf_energy < 5:
        number_of_materials_in_box.append(current_material)
        continue

    taking_box += 1

    if taking_box % 3 == 0:
        needed_energy = current_material * 2
        if current_elf_energy >= needed_energy:
            made_toys += 2
            total_used_energy += needed_energy
            current_elf_energy -= needed_energy
            elf_energy.append(current_elf_energy + 1)
            if taking_box % 5 == 0:
                made_toys -= 2
                elf_energy[-1] -= 1
        else:
            number_of_materials_in_box.append(current_material)
            current_elf_energy *= 2
            elf_energy.append(current_elf_energy)
            continue

    elif taking_box % 5 == 0:
        if current_elf_energy >= current_material:
            total_used_energy += current_material
            current_elf_energy -= current_material
            elf_energy.append(current_elf_energy)
            if taking_box % 3 == 0:
                made_toys -= 2
        else:
            number_of_materials_in_box.append(current_material)
            current_elf_energy *= 2
            elf_energy.append(current_elf_energy)
            continue

    elif current_elf_energy >= current_material:
        made_toys += 1
        total_used_energy += current_material
        current_elf_energy -= current_material
        elf_energy.append(current_elf_energy + 1)
    else:
        number_of_materials_in_box.append(current_material)
        current_elf_energy *= 2
        elf_energy.append(current_elf_energy)
        continue

print(f'Toys: {made_toys}')
print(f'Energy: {total_used_energy}')
if elf_energy:
    print(f'Elves left: {", ".join(map(str, elf_energy))}')
if number_of_materials_in_box:
    print(f'Boxes left: {", ".join(map(str, number_of_materials_in_box))}')
