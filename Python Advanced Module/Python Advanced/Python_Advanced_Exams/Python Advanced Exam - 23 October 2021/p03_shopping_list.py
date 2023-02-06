def shopping_list(budget, **kwargs):
    products_type = 0
    bought_products = {}
    kwargs_copy = kwargs.copy()

    if budget < 100:
        return 'You do not have enough budget.'
    else:
        for product, product_data in kwargs_copy.items():
            if products_type >= 5:
                break
            elif products_type < 5 and not kwargs:
                break
            quantity = product_data[0]
            price = product_data[1]

            total_sum = quantity * price

            if total_sum <= budget:
                products_type += 1
                budget -= total_sum
                bought_products[product] = total_sum
                del kwargs[product]

    output = ''

    for product, price in bought_products.items():
        output += f'You bought {product} for {price:.2f} leva.\n'

    return output

# --- TEST CODE --
# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))
#
# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))
#
# print(shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),
#                     juice=(2, 3),
#                     eggs=(3, 1),
#                     ))
