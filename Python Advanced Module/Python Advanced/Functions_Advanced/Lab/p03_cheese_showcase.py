def sorting_cheeses(**kwargs):
    sorted_cheese = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for name, quantity in sorted_cheese:
        result += name + '\n'
        sorted_quantity = sorted(quantity, reverse=True)
        result += "\n".join(map(str, sorted_quantity)) + "\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
