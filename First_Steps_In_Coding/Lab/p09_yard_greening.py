area = float(input())
price_for_area = area * 7.61
discount = price_for_area * 18/100
price_after_discount = price_for_area - discount
print(f"The final price is: {price_after_discount} lv.")
print(f"The discount is: {discount} lv.")