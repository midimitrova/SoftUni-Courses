class MinerTask:

    def __init__(self, current_resource, current_quantity):
        self.current_resource = current_resource
        self.current_quantity = current_quantity
        self.collection = {}

    def collect(self):
        while True:
            if self.current_resource not in self.collection.keys():
                self.collection[self.current_resource] = 0
            self.collection[self.current_resource] += self.current_quantity
            self.current_resource = input()
            if self.current_resource == 'stop':
                break
            self.current_quantity = int(input())

    def __repr__(self):
        result = ''
        for key, value in self.collection.items():
            result += f"{key} -> {value}\n"
        return result


resource = input()
quantity = int(input())
miner_task = MinerTask(resource, quantity)
miner_task.collect()
print(miner_task)
