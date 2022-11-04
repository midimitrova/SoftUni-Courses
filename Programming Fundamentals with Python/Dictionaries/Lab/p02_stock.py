class Bakery:

    def __init__(self, stock_of_products, searched_items):
        self.bakery = {}
        self.product = ''
        self.quantity = ''
        self.stock_of_products = stock_of_products
        self.searched_items = searched_items

    def make_dict(self):
        for product_index in range(0, len(self.stock_of_products), 2):
            self.product = self.stock_of_products[product_index]
            self.quantity = self.stock_of_products[product_index + 1]
            self.bakery[self.product] = int(self.quantity)

    def searched_products(self):
        for item in self.searched_items:
            if item in self.bakery.keys():
                print(f"We have {self.bakery[item]} of {item} left")
            else:
                print(f"Sorry, we don't have {item}")


elements = input().split()
searched_products = input().split()
bakery = Bakery(elements, searched_products)
bakery.make_dict()
bakery.searched_products()
