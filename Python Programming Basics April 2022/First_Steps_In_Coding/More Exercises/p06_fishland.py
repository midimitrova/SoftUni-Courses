price_skumria = float(input())
price_caca = float(input())
quantity_palamud = float(input())
quantity_safrid = float(input())
quantity_midi = float(input())


price_palamud = price_skumria + (price_skumria * 60/100)
price_safrid = price_caca + (price_caca * 80/100)
price_midi = 7.50

total_price = price_palamud * quantity_palamud + price_safrid * quantity_safrid + price_midi * quantity_midi

print("{:.2f}".format(total_price))
