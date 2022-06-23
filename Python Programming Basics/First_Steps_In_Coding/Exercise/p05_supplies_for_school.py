number_of_package_pens = int(input())
number_of_package_markers = int(input())
Litre_preparat = int(input())
discount = int(input())/100

price_pen = number_of_package_pens * 5.80
price_markers = number_of_package_markers * 7.20
price_preparat = Litre_preparat * 1.20
total = price_pen + price_markers + price_preparat
price_with_discount = total - (total * discount)
print(price_with_discount)