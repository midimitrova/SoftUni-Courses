from collections import deque


def stock_availability(*args):
    inventory_list = deque(args[0])

    command = args[1]
    other_parameters = list(args[2:])

    if command == 'delivery':
        inventory_list.extend(other_parameters)
    elif command == 'sell':
        if not other_parameters:
            inventory_list.popleft()
        elif str(other_parameters[0]).isdigit():
            for cupcake in range(other_parameters[0]):
                inventory_list.popleft()
        else:
            while other_parameters:
                while other_parameters[0] in inventory_list:
                    inventory_list.remove(other_parameters[0])
                other_parameters.pop(0)
    return list(inventory_list)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
