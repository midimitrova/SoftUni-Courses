class MinerTask:

    def __init__(self):
        self.collection = {}

    def collect(self, current_resource, current_quantity):
        if current_resource not in self.collection.keys():
            self.collection[current_resource] = 0
        self.collection[current_resource] += current_quantity

    def __repr__(self):
        result = ''
        for key, value in self.collection.items():
            result += f"{key} -> {value}\n"
        return result


miner_task = MinerTask()
while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = int(input())
    miner_task.collect(resource, quantity)
print(miner_task)