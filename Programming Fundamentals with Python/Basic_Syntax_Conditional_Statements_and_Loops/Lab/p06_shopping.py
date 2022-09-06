budget = int(input())

total_price = 0

command = input()
while command != 'End':
    price = int(command)

    total_price += price

    if total_price > budget:
        break

    command = input()

if budget >= total_price:
    print("You bought everything needed.")
elif total_price > budget:
    print("You went in overdraft!")


