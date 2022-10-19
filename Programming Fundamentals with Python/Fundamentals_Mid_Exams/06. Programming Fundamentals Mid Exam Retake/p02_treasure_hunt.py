treasure = input().split('|')

command = input().split()

while command[0] != "Yohoho!":
    treasure_hunt = command[0]

    if treasure_hunt == 'Loot':
        items = command[1:]
        for item in items:
            if item not in treasure:
                treasure.insert(0, item)
    elif treasure_hunt == 'Drop':
        index = int(command[1])
        if index in range(len(treasure)):
            popped_item = treasure.pop(index)
            treasure.append(popped_item)
    elif treasure_hunt == 'Steal':
        count = int(command[1])
        stolen_items = []
        if count >= len(treasure):
            removed = treasure
            print(', '.join(removed))
            print('Failed treasure hunt.')
            exit()
        else:
            for _ in range(count):
                popped = treasure.pop()
                stolen_items.insert(0, popped)
            print(', '.join(stolen_items))

    command = input().split()

lenght_item = 0
for item in treasure:
    lenght_item += len(item)

if len(treasure) > 0:
    average_treasure = lenght_item / len(treasure)
    print(f"Average treasure gain: {average_treasure:.2f} pirate credits.")