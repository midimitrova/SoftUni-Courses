class Bakery:

    def __init__(self, data):
        self.bakery = {}
        self.product = ''
        self.quantity = ''
        self.data = data

    def receive_products(self):
        while self.data != "statistics":
            self.product, self.quantity = self.data.split(': ')
            self.quantity = int(self.quantity)

            if self.product not in self.bakery.keys():
                self.bakery[self.product] = 0
            self.bakery[self.product] += self.quantity
            self.data = input()

    def display_dict(self):
        print("Products in stock:")
        for key, value in self.bakery.items():
            print(f'- {key}: {value}')
        print(f'Total Products: {len(self.bakery)}')
        print(f'Total Quantity: {sum(self.bakery.values())}')


command = input()
bakery = Bakery(command)
bakery.receive_products()
bakery.display_dict()
