command = input()

total_price_without_tax = 0
total_taxes = 0
total_price_with_taxes = 0
command_list = []

while True:

    command_list.append(command)

    if command == 'regular' or command == 'special':
        break

    price = float(command)

    if price < 0:
        print("Invalid price!")
        command = input()
        continue

    total_price_without_tax += price

    command = input()

total_taxes = total_price_without_tax * 20/100
total_price_with_taxes = total_taxes + total_price_without_tax

last_command = command_list.pop()
if last_command == 'special':
    total_price_with_taxes -= total_price_with_taxes * 10/100

if total_price_with_taxes == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price_without_tax:.2f}$')
    print(f'Taxes: {total_taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_price_with_taxes:.2f}$')





