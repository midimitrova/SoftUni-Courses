from collections import deque

firework_data = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}
are_collected = 0

firework_effects = deque([int(x) for x in input().split(', ')])
explosive_power = deque([int(x) for x in input().split(', ')])

while firework_effects and explosive_power:

    current_effect = firework_effects.popleft()
    current_power = explosive_power.pop()

    if current_effect <= 0 and current_power <= 0:
        continue
    if current_effect <= 0:
        explosive_power.append(current_power)
        continue
    if current_power <= 0:
        firework_effects.appendleft(current_effect)
        continue

    result = current_effect + current_power

    if result % 15 == 0:
        firework_data['Crossette Fireworks'] += 1
    elif result % 3 == 0:
        firework_data['Palm Fireworks'] += 1
    elif result % 5 == 0:
        firework_data['Willow Fireworks'] += 1
    else:
        firework_effects.append(current_effect - 1)
        explosive_power.append(current_power)

    if firework_data['Crossette Fireworks'] >= 3 and firework_data['Palm Fireworks'] >= 3\
            and firework_data['Willow Fireworks'] >=3:
        are_collected = True
        break

    if are_collected:
        break

if are_collected:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")
for firework, value in firework_data.items():
    print(f"{firework}: {value}")