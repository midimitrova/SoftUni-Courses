class Zoo:
    __animals = 0

    def __init__(self, name_zoo):
        self.name_zoo = name_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result += f"Mammals in {self.name_zoo}: {', '.join(self.mammals)}\n"
        elif species == 'fish':
            result += f"Fishes in {self.name_zoo}: {', '.join(self.fishes)}\n"
        elif species == 'bird':
            result += f"Birds in {self.name_zoo}: {', '.join(self.birds)}\n"

        result += f'Total animals: {Zoo.__animals}'
        return result


zoo_name = input()
number_animals = int(input())
zoo = Zoo(zoo_name)

for _ in range(number_animals):
    type_animal, animal = input().split()
    zoo.add_animal(type_animal, animal)

info = input()
print(zoo.get_info(info))
