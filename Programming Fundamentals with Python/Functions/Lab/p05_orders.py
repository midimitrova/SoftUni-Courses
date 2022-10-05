def calculations(product, quantity):
    if product == 'coffee':
        return quantity * price_coffee
    elif product == 'water':
        return quantity * price_water
    elif product == 'coke':
        return quantity * price_coke
    elif product == 'snacks':
        return quantity * price_snacks


price_coffee = 1.50
price_water = 1.00
price_coke = 1.40
price_snacks = 2.00

purchase = input()
amount = int(input())
total_price = calculations(purchase, amount)
print(f'{total_price:.2f}')