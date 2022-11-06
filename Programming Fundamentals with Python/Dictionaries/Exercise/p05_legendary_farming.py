class Farming:

    def __init__(self, items):
        self.items = items
        self.collection_of_items = {"shards": 0, "fragments": 0, "motes": 0}
        self.quantity = 0
        self.item = ''
        self.is_obtained = False

    def collect_items(self):
        while not self.is_obtained:
            for index in range(0, len(self.items), 2):
                self.quantity = int(self.items[index])
                self.item = self.items[index + 1].lower()
                if self.item not in self.collection_of_items.keys():
                    self.collection_of_items[self.item] = 0
                self.collection_of_items[self.item] += self.quantity

                if self.collection_of_items["shards"] >= 250:
                    print("Shadowmourne obtained!")
                    self.is_obtained = True
                    self.collection_of_items["shards"] -= 250
                elif self.collection_of_items["fragments"] >= 250:
                    print("Valanyr obtained!")
                    self.is_obtained = True
                    self.collection_of_items["fragments"] -= 250
                elif self.collection_of_items["motes"] >= 250:
                    print("Dragonwrath obtained!")
                    self.is_obtained = True
                    self.collection_of_items["motes"] -= 250
                if self.is_obtained:
                    break
            if self.is_obtained:
                break

            self.items = input().split()

        for item, quantity in self.collection_of_items.items():
            print(f"{item}: {quantity}")


data = input().split()
farming = Farming(data)
farming.collect_items()
