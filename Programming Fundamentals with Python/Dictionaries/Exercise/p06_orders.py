class Orders:

    def __init__(self, data):
        self.data = data
        self.products_dict = {}
        self.product = ''
        self.price = 0
        self.quantity = 0

    def collect_products(self):
        while self.data[0] != 'buy':
            self.product = self.data[0]
            self.price = float(self.data[1])
            self.quantity = int(self.data[2])

            if self.product not in self.products_dict.keys():
                self.products_dict[self.product] = []
                self.products_dict[self.product].append(self.price)
                self.products_dict[self.product].append(self.quantity)
            else:
                self.products_dict[self.product][0] = self.price
                self.products_dict[self.product][1] += self.quantity

            self.data = input().split()

    def __repr__(self):
        result = ''
        for key, value in self.products_dict.items():
            total_price = value[0] * value[1]
            result += f"{key} -> {total_price:.2f}\n"
        return result


command = input().split()
order = Orders(command)
order.collect_products()
print(order)
