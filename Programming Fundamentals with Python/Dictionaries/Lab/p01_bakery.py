class Bakery:

    def __init__(self):
        self.bakery = {}
        self.product = ''
        self.quantity = ''

    def make_dict(self):
        for i in range(0, len(elements), 2):
            self.product = elements[i]
            self.quantity = elements[i + 1]
            self.bakery[self.product] = int(self.quantity)

    def display_dict(self):
        print(self.bakery)


elements = input().split()
bakery = Bakery()
bakery.make_dict()
bakery.display_dict()
