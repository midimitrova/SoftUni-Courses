class Bakery:

    def __init__(self, stock_of_products):
        self.bakery = {}
        self.product = ''
        self.quantity = ''
        self.stock_of_products = stock_of_products

    def make_dict(self):
        for product_index in range(0, len(self.stock_of_products), 2):
            self.product = self.stock_of_products[product_index]
            self.quantity = self.stock_of_products[product_index + 1]
            self.bakery[self.product] = int(self.quantity)

    def display_dict(self):
        print(self.bakery)


elements = input().split()
bakery = Bakery(elements)
bakery.make_dict()
bakery.display_dict()
