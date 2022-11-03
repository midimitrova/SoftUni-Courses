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

    def searched_products(self):
        for item in searched_products:
            if item in self.bakery.keys():
                print(f"We have {self.bakery[item]} of {item} left")
            else:
                print(f"Sorry, we don't have {item}")


elements = input().split()
searched_products = input().split()
bakery = Bakery()
bakery.make_dict()
bakery.searched_products()
