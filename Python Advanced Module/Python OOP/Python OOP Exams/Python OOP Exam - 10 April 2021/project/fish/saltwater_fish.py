from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 5, price)
        self.fish_type = 'SaltwaterFish'

    def eat(self):
        self.size += 2
