number_of_heroes = int(input())
heroes = {}

max_hp = 100
max_mp = 200

for _ in range(number_of_heroes):
    data = input().split()
    hero_name = data[0]
    hit_points = int(data[1])
    mana_points = int(data[2])
    heroes[hero_name] = [hit_points, mana_points]

command = input().split(' - ')

while command[0] != 'End':

    if command[0] == 'CastSpell':
        name_hero = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes[name_hero][1] >= mp_needed:
            heroes[name_hero][1] -= mp_needed
            print(f'{name_hero} has successfully cast {spell_name} and now has {heroes[name_hero][1]} MP!')
        else:
            print(f'{name_hero} does not have enough MP to cast {spell_name}!')
    elif command[0] == 'TakeDamage':
        name_hero = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes[name_hero][0] -= damage
        if heroes[name_hero][0] > 0:
            print(f'{name_hero} was hit for {damage} HP by {attacker} and now has {heroes[name_hero][0]} HP left!')
        else:
            print(f'{name_hero} has been killed by {attacker}!')
            heroes.pop(name_hero)
    elif command[0] == 'Recharge':
        name_hero = command[1]
        amount = int(command[2])
        needed_mp = max_mp - heroes[name_hero][1]
        heroes[name_hero][1] += amount
        if heroes[name_hero][1] > max_mp:
            heroes[name_hero][1] = max_mp
            print(f'{name_hero} recharged for {needed_mp} MP!')
        else:
            print(f'{name_hero} recharged for {amount} MP!')
    elif command[0] == 'Heal':
        name_hero = command[1]
        amount = int(command[2])
        needed_hp = max_hp - heroes[name_hero][0]
        heroes[name_hero][0] += amount
        if heroes[name_hero][0] > max_hp:
            heroes[name_hero][0] = max_hp
            print(f'{name_hero} healed for {needed_hp} HP!')
        else:
            print(f'{name_hero} healed for {amount} HP!')

    command = input().split(' - ')

if heroes:
    for name, value in heroes.items():
        print(f'{name}\n  HP: {heroes[name][0]}\n  MP: {heroes[name][1]}')
