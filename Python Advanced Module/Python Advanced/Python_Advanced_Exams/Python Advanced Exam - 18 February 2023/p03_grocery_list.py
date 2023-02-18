from collections import deque


def shop_from_grocery_list(budget, *args):
    budget = int(budget)
    grocery_list = list(args[0])
    shopping = deque(args[1:])

    while grocery_list and shopping:
        purchase = shopping.popleft()
        purchase_item = purchase[0]
        price = float(purchase[1])

        if budget < price:
            break
        if purchase_item in grocery_list:
            budget -= price
            grocery_list.remove(purchase_item)
        else:
            continue

    if grocery_list:
        output = f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."
    else:
        output = f"Shopping is successful. Remaining budget: {budget:.2f}."

    return output



# --- TEST CODE ---
# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("tomato", 20.45),
# ))
#
# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))
#
#
# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat", "chocolate"],
#     ("cola", 15.8),
#     ("chocolate", 30),
#     ("tomato", 15.85),
#     ("chips", 50),
#     ("meat", 22.99),
# ))

