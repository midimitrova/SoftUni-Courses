from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = deque([int(x) for x in input().split(', ')])

bombs = {
    'Datura Bombs': [40, 0],
    'Cherry Bombs': [60, 0],
    'Smoke Decoy Bombs': [120, 0],
}

are_made = False

while bomb_effects and bomb_casings:

    current_bomb_effect = bomb_effects.popleft()
    current_bomb_casing = bomb_casings.pop()

    current_sum = current_bomb_effect + current_bomb_casing

    for bomb, value in bombs.items():

        if current_sum == value[0]:
            bombs[bomb][1] += 1
            break
    else:
        bomb_casings.append(current_bomb_casing - 5)
        bomb_effects.appendleft(current_bomb_effect)

    if bombs['Datura Bombs'][1] >= 3 and bombs['Cherry Bombs'][1] >= 3 and bombs['Smoke Decoy Bombs'][1] >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        are_made = True
        break

if not are_made:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
else:
    print("Bomb Casings: empty")
for bomb, value in sorted(bombs.items()):
    print(f'{bomb}: {value[1]}')
