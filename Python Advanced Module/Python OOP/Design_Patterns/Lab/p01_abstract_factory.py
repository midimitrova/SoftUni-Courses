from abc import ABC, abstractmethod


class Chair:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Sofa:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Table:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class AbstractFactory(ABC):

    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass

    @abstractmethod
    def create_table(self):
        pass


class VictorianFactory(AbstractFactory):

    def create_chair(self):
        return Chair('victorian chair')

    def create_sofa(self):
        return Sofa('victorian sofa')

    def create_table(self):
        return Table('victorian table')


class ModernFactory(AbstractFactory):

    def create_chair(self):
        return Chair('modern chair')

    def create_sofa(self):
        return Sofa('modern sofa')

    def create_table(self):
        return Table('modern table')


class FuturisticFactory(AbstractFactory):

    def create_chair(self):
        return Chair('futuristic chair')

    def create_sofa(self):
        return Sofa('futuristic sofa')

    def create_table(self):
        return Table('futuristic table')


def get_factory(style):
    if style == 'Victorian':
        return VictorianFactory()

    elif style == 'Modern':
        return ModernFactory()

    elif style == 'Futuristic':
        return FuturisticFactory()


if __name__ == '__main__':
    client_style = input().title()
    factory = get_factory(client_style)
    print(factory.create_chair())
