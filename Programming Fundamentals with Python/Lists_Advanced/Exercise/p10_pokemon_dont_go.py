distances_to_the_pokemon = [int(num) for num in input().split()]

elements = []
while True:
    index = int(input())

    if 0 <= index < len(distances_to_the_pokemon):
        popped_item = distances_to_the_pokemon.pop(index)
        elements.append(popped_item)
        for i in range(len(distances_to_the_pokemon)):
            if distances_to_the_pokemon[i] <= popped_item:
                distances_to_the_pokemon[i] += popped_item
            else:
                distances_to_the_pokemon[i] -= popped_item
    elif index < 0:
        popped_item = distances_to_the_pokemon.pop(0)
        elements.append(popped_item)
        last_element = distances_to_the_pokemon[-1]
        distances_to_the_pokemon.insert(0, last_element)
        for i in range(len(distances_to_the_pokemon)):
            if distances_to_the_pokemon[i] <= popped_item:
                distances_to_the_pokemon[i] += popped_item
            else:
                distances_to_the_pokemon[i] -= popped_item
    elif index >= len(distances_to_the_pokemon):
        popped_item = distances_to_the_pokemon.pop(-1)
        elements.append(popped_item)
        first_element = distances_to_the_pokemon[0]
        distances_to_the_pokemon.append(first_element)
        for i in range(len(distances_to_the_pokemon)):
            if distances_to_the_pokemon[i] <= popped_item:
                distances_to_the_pokemon[i] += popped_item
            else:
                distances_to_the_pokemon[i] -= popped_item

    if len(distances_to_the_pokemon) == 0:
        break

print(sum(elements))
