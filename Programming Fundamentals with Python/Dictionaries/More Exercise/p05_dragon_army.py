dragon_army = {}

number_of_commands = int(input())

for _ in range(number_of_commands):
    type_dragon, name, damage, health, armor = input().split()

    if damage == 'null':
        damage = 45
    if health == 'null':
        health = 250
    if armor == 'null':
        armor = 10

    damage = int(damage)
    health = int(health)
    armor = int(armor)

    if type_dragon not in dragon_army.keys():
        dragon_army[type_dragon] = {name: [damage, health, armor]}
    elif type_dragon in dragon_army.keys() and name in dragon_army[type_dragon].keys():
        dragon_army[type_dragon][name] = [damage, health, armor]
    elif type_dragon in dragon_army.keys() and name not in dragon_army[type_dragon].keys():
        dragon_army[type_dragon][name] = [damage, health, armor]

for type in dragon_army:
    damage, health, armor = 0, 0, 0
    for name in dragon_army[type]:
        damage += dragon_army[type][name][0]
        health += dragon_army[type][name][1]
        armor += dragon_army[type][name][2]
    total_dragons = len(dragon_army[type])
    print(f"{type}::({(damage / total_dragons):.2f}/{(health / total_dragons):.2f}/{(armor / total_dragons):.2f})")
    for name in sorted(dragon_army[type].keys()):
        print(
            f"-{name} -> damage: {dragon_army[type][name][0]}, health: {dragon_army[type][name][1]},"
            f" armor: {dragon_army[type][name][2]}")
