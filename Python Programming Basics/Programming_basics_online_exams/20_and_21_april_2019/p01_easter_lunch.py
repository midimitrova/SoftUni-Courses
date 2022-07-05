number_kozunak = int(input())
number_kori_eggs = int(input())
kg_kurabii = int(input())

price_kozunak = 3.20
price_eggs = 4.35
price_kurabii_kg = 5.40
price_paint = 0.15

final_price_kozunak = number_kozunak * price_kozunak
final_price_kurabii = kg_kurabii * price_kurabii_kg
final_price_eggs = number_kori_eggs * price_eggs
paint = price_paint * number_kori_eggs * 12

total_price = final_price_kozunak + final_price_kurabii + final_price_eggs + paint

print(f"{total_price:.2f}")