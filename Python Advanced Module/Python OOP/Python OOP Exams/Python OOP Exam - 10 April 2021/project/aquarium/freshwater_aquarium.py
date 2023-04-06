from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):

    def __init__(self, name):
        self.name = name
        self.capacity = 50
        self.decorations = []
        self.fish = []
        self.type = 'FreshwaterAquarium'