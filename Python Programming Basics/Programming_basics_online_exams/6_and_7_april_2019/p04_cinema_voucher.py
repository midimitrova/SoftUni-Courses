price_voucher = int(input())

price_ticket = 0

ticket_cnt = 0
product_cnt = 0

name = input()


while name != "End":

    lenght = len(name)



    if lenght > 8:

        price_ticket = ord(name[0]) + ord(name[1])
        if price_voucher >= price_ticket:
            price_voucher -= price_ticket
            ticket_cnt += 1
        else:
            break
    elif lenght <= 8:

        price_ticket = ord(name[0])

        if price_voucher >= price_ticket:
            price_voucher -= price_ticket
            product_cnt += 1
        else:
            break

    name = input()


if name == "End" or price_ticket > price_voucher:
    print(f"{ticket_cnt}")
    print(f"{product_cnt}")

