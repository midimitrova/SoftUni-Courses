import re


class Furniture:

    def __init__(self, text):
        self.text = text
        self.bought_furniture = []
        self.total_price = 0

    def get_furniture(self):
        pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)\b'
        while self.text != 'Purchase':
            matches = re.search(pattern, self.text)
            if matches:
                furnitures, price, quantity = matches.groups()
                self.bought_furniture.append(furnitures)
                self.total_price += float(price) * int(quantity)
            self.text = input()

    def display(self):
        print('Bought furniture:')
        if self.bought_furniture:
            print('\n'.join(self.bought_furniture))
        print(f'Total money spend: {self.total_price:.2f}')


data = input()
furniture = Furniture(data)
furniture.get_furniture()
furniture.display()
