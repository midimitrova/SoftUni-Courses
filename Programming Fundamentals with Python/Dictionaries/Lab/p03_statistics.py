class Bakery:

    def __init__(self):
        self.bakery = {}
        self.product = ''
        self.quantity = ''

    def receive_products(self):
        data = input()
        while data != "statistics":
            self.product, self.quantity = data.split(': ')
            self.quantity = int(self.quantity)

            if self.product not in self.bakery.keys():
                self.bakery[self.product] = 0
            self.bakery[self.product] += self.quantity
            data = input()

    def display_dict(self):
        print("Products in stock:")
        for key, value in self.bakery.items():
            print(f'- {key}: {value}')
        print(f'Total Products: {len(self.bakery)}')
        print(f'Total Quantity: {sum(self.bakery.values())}')


bakery = Bakery()
bakery.receive_products()
bakery.display_dict()
