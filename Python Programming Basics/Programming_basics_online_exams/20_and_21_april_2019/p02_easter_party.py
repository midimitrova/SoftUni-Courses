number_guests = int(input())
price_for_one_guest = float(input())
budget = float(input())

cake = budget * 10/100
sum = number_guests * price_for_one_guest

if 10 <= number_guests <= 15:
    discount = sum * 15/100
    sum -= discount
elif 15 < number_guests <= 20:
    discount = sum * 20/100
    sum -= discount
elif number_guests > 20:
    discount = sum * 25/100
    sum -= discount

final_price = cake + sum

if budget >= final_price:
    print(f"It is party time! {budget - final_price:.2f} leva left.")
else:
    print(f"No party! {final_price - budget:.2f} leva needed.")