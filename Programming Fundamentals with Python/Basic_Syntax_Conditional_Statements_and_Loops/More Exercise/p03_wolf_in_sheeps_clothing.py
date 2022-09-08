animals = input().split(', ')

is_eaten = False


for i in range(len(animals)):
    if animals.index('wolf') == len(animals) - 1:
        is_eaten = False
    elif animals.index('wolf') == i:
        eaten_animal = len(animals) - animals.index("wolf") - 1
        is_eaten = True


if is_eaten == False:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {eaten_animal}! You are about to be eaten by a wolf!")

